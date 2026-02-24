"""
Poetic Goblin — File Storage Abstraction
Supports local filesystem (dev) and AWS S3 (prod).
"""
import os
import uuid
from werkzeug.utils import secure_filename
from config import Config

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_upload(file_obj, subfolder='avatars'):
    """
    Save an uploaded file. Returns the public URL.
    - Dev: saves to static/uploads/ and returns /static/uploads/... path
    - Prod: uploads to S3 and returns the S3/CDN URL
    """
    if not file_obj or not file_obj.filename:
        return ''
    if not allowed_file(file_obj.filename):
        return ''

    ext = file_obj.filename.rsplit('.', 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{ext}"

    if Config.STORAGE_TYPE == 's3':
        return _save_to_s3(file_obj, filename, subfolder)
    else:
        return _save_local(file_obj, filename, subfolder)


def _save_local(file_obj, filename, subfolder):
    """Save to local static/uploads/ directory."""
    upload_dir = os.path.join(Config.UPLOAD_FOLDER, subfolder)
    os.makedirs(upload_dir, exist_ok=True)
    filepath = os.path.join(upload_dir, filename)
    file_obj.save(filepath)
    # Return URL relative to static
    return f"/static/uploads/{subfolder}/{filename}"


def _save_to_s3(file_obj, filename, subfolder):
    """Upload to AWS S3 and return the public URL."""
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
        content_type = file_obj.content_type or 'application/octet-stream'

        s3.upload_fileobj(
            file_obj,
            Config.AWS_S3_BUCKET,
            key,
            ExtraArgs={
                'ContentType': content_type,
                'ACL': 'public-read',
            }
        )

        # Return the public URL
        if Config.AWS_S3_CUSTOM_DOMAIN:
            return f"https://{Config.AWS_S3_CUSTOM_DOMAIN}/{key}"
        return f"https://{Config.AWS_S3_BUCKET}.s3.{Config.AWS_S3_REGION}.amazonaws.com/{key}"

    except Exception as e:
        print(f"[Poetic Goblin] S3 upload failed: {e}")
        # Fallback to local storage
        return _save_local(file_obj, filename, subfolder)
