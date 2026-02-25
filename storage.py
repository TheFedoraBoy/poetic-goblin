"""
Poetic Goblin — File Storage Abstraction
Supports local filesystem (dev) and AWS S3 / Cloudflare R2 (prod).

Security:
  - Validates file extension AND magic bytes (prevents disguised uploads)
  - Resizes images to max 1920px wide (saves bandwidth + storage)
  - Strips EXIF metadata (protects user privacy)
"""
import os
import io
import uuid
from werkzeug.utils import secure_filename
from config import Config

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Magic byte signatures for image types
MAGIC_BYTES = {
    'jpg':  [b'\xff\xd8\xff'],
    'jpeg': [b'\xff\xd8\xff'],
    'png':  [b'\x89PNG\r\n\x1a\n'],
    'gif':  [b'GIF87a', b'GIF89a'],
    'webp': [b'RIFF'],  # RIFF....WEBP
}

MAX_IMAGE_DIMENSION = 1920  # Max width/height in pixels


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def _validate_magic_bytes(file_obj, ext):
    """Check that the file's magic bytes match the claimed extension."""
    header = file_obj.read(12)
    file_obj.seek(0)

    if ext not in MAGIC_BYTES:
        return False

    for signature in MAGIC_BYTES[ext]:
        if header[:len(signature)] == signature:
            if ext == 'webp' and header[8:12] != b'WEBP':
                return False
            return True
    return False


def _process_image(file_obj, ext):
    """
    Resize image if too large and strip EXIF metadata.
    Returns a BytesIO object ready for saving/uploading.
    Falls back to raw file if Pillow is not installed.
    """
    try:
        from PIL import Image

        img = Image.open(file_obj)

        # Convert RGBA to RGB for JPEG
        if ext in ('jpg', 'jpeg') and img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if 'A' in img.mode else None)
            img = background

        # Resize if larger than max dimension
        if max(img.size) > MAX_IMAGE_DIMENSION:
            img.thumbnail((MAX_IMAGE_DIMENSION, MAX_IMAGE_DIMENSION), Image.LANCZOS)

        # Save to buffer WITHOUT EXIF data
        output = io.BytesIO()
        save_kwargs = {}
        if ext in ('jpg', 'jpeg'):
            save_format = 'JPEG'
            save_kwargs = {'quality': 85, 'optimize': True}
        elif ext == 'png':
            save_format = 'PNG'
            save_kwargs = {'optimize': True}
        elif ext == 'webp':
            save_format = 'WEBP'
            save_kwargs = {'quality': 85}
        elif ext == 'gif':
            save_format = 'GIF'
        else:
            save_format = 'PNG'

        img.save(output, format=save_format, **save_kwargs)
        output.seek(0)
        return output

    except ImportError:
        print("[Poetic Goblin] Warning: Pillow not installed. Images not resized.")
        file_obj.seek(0)
        return file_obj
    except Exception as e:
        print(f"[Poetic Goblin] Image processing error: {e}")
        file_obj.seek(0)
        return file_obj


def save_upload(file_obj, subfolder='avatars'):
    """
    Save an uploaded file. Returns the public URL.
    Validates extension + magic bytes, resizes + strips EXIF.
    """
    if not file_obj or not file_obj.filename:
        return ''
    if not allowed_file(file_obj.filename):
        return ''

    ext = file_obj.filename.rsplit('.', 1)[1].lower()

    if not _validate_magic_bytes(file_obj, ext):
        print(f"[Poetic Goblin] Rejected upload: magic bytes don't match .{ext}")
        return ''

    processed = _process_image(file_obj, ext)
    filename = f"{uuid.uuid4().hex}.{ext}"

    if Config.STORAGE_TYPE == 's3':
        return _save_to_s3(processed, filename, subfolder, ext)
    else:
        return _save_local(processed, filename, subfolder)


def _save_local(file_obj, filename, subfolder):
    """Save to local static/uploads/ directory."""
    upload_dir = os.path.join(Config.UPLOAD_FOLDER, subfolder)
    os.makedirs(upload_dir, exist_ok=True)
    filepath = os.path.join(upload_dir, filename)

    if hasattr(file_obj, 'read'):
        data = file_obj.read()
        with open(filepath, 'wb') as f:
            f.write(data)
    else:
        file_obj.save(filepath)

    return f"/static/uploads/{subfolder}/{filename}"


def _save_to_s3(file_obj, filename, subfolder, ext):
    """Upload to AWS S3 / Cloudflare R2 and return the public URL."""
    try:
        import boto3
        from botocore.config import Config as BotoConfig

        s3_kwargs = dict(
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
            region_name=Config.AWS_S3_REGION,
            config=BotoConfig(signature_version='s3v4'),
        )
        if Config.AWS_S3_ENDPOINT_URL:
            s3_kwargs['endpoint_url'] = Config.AWS_S3_ENDPOINT_URL

        s3 = boto3.client('s3', **s3_kwargs)

        key = f"uploads/{subfolder}/{filename}"
        content_types = {
            'jpg': 'image/jpeg', 'jpeg': 'image/jpeg',
            'png': 'image/png', 'gif': 'image/gif', 'webp': 'image/webp',
        }
        content_type = content_types.get(ext, 'application/octet-stream')

        s3.upload_fileobj(
            file_obj,
            Config.AWS_S3_BUCKET,
            key,
            ExtraArgs={
                'ContentType': content_type,
                'CacheControl': 'public, max-age=31536000',
            }
        )

        if Config.AWS_S3_CUSTOM_DOMAIN:
            return f"https://{Config.AWS_S3_CUSTOM_DOMAIN}/{key}"
        if Config.AWS_S3_ENDPOINT_URL:
            return f"{Config.AWS_S3_ENDPOINT_URL}/{Config.AWS_S3_BUCKET}/{key}"
        return f"https://{Config.AWS_S3_BUCKET}.s3.{Config.AWS_S3_REGION}.amazonaws.com/{key}"

    except Exception as e:
        print(f"[Poetic Goblin] S3 upload failed: {e}")
        return _save_local(file_obj, filename, subfolder)
