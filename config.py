"""
Poetic Goblin — Configuration
All settings from environment variables with sensible dev defaults.
"""
import os

class Config:
    """Base configuration — dev-friendly defaults."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'poetic-goblin-dev-key-CHANGE-IN-PRODUCTION')

    # ─── Database ─────────────────────────────────────────────────────
    # Set DB_TYPE=mysql or DB_TYPE=postgres for production. Default: sqlite (zero-config dev)
    # You can also set DATABASE_URL for one-line config (common on Railway/Render/Heroku)
    DB_TYPE = os.environ.get('DB_TYPE', 'sqlite')  # 'sqlite', 'mysql', or 'postgres'
    DATABASE_URL = os.environ.get('DATABASE_URL', '')  # Overrides DB_TYPE if set

    # SQLite (dev)
    SQLITE_PATH = os.environ.get('SQLITE_PATH', os.path.join(os.path.dirname(__file__), 'poetic_goblin.db'))

    # MySQL (prod)
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'poetic_goblin')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'poetic_goblin')

    # PostgreSQL (prod)
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = int(os.environ.get('POSTGRES_PORT', 5432))
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'poetic_goblin')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
    POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'poetic_goblin')

    # ─── File Storage ─────────────────────────────────────────────────
    # Set STORAGE_TYPE=s3 for production. Default: local
    STORAGE_TYPE = os.environ.get('STORAGE_TYPE', 'local')  # 'local' or 's3'

    # Local (dev)
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER',
                                   os.path.join(os.path.dirname(__file__), 'static', 'uploads'))

    # S3 (prod) — also works with S3-compatible services like Cloudflare R2
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_S3_BUCKET = os.environ.get('AWS_S3_BUCKET', '')
    AWS_S3_REGION = os.environ.get('AWS_S3_REGION', 'us-east-1')
    AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN', '')  # e.g. CDN URL
    AWS_S3_ENDPOINT_URL = os.environ.get('AWS_S3_ENDPOINT_URL', '')  # For R2/MinIO

    # ─── Email ────────────────────────────────────────────────────────
    # Set EMAIL_TYPE=resend (recommended) or EMAIL_TYPE=smtp for production.
    # Default: console (prints to terminal)
    EMAIL_TYPE = os.environ.get('EMAIL_TYPE', 'console')  # 'console', 'smtp', or 'resend'

    # Resend API (recommended — simplest setup)
    RESEND_API_KEY = os.environ.get('RESEND_API_KEY', '')

    SMTP_HOST = os.environ.get('SMTP_HOST', 'smtp.gmail.com')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
    SMTP_USER = os.environ.get('SMTP_USER', '')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', '')
    SMTP_FROM_NAME = os.environ.get('SMTP_FROM_NAME', 'Poetic Goblin')
    SMTP_FROM_EMAIL = os.environ.get('SMTP_FROM_EMAIL', 'poeticgoblin@gmail.com')
    SMTP_USE_TLS = os.environ.get('SMTP_USE_TLS', 'true').lower() == 'true'

    # ─── App Settings ─────────────────────────────────────────────────
    BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_UPLOAD_MB', 16)) * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

    # Rate limiting
    RATELIMIT_ENABLED = os.environ.get('RATELIMIT_ENABLED', 'true').lower() == 'true'
    RATELIMIT_STORAGE_URI = os.environ.get('RATELIMIT_STORAGE_URI', 'memory://')
    # For production with Redis: 'redis://localhost:6379'

    # Email verification
    REQUIRE_EMAIL_VERIFICATION = os.environ.get('REQUIRE_EMAIL_VERIFICATION', 'false').lower() == 'true'

    # Token expiry (hours)
    VERIFICATION_TOKEN_HOURS = int(os.environ.get('VERIFICATION_TOKEN_HOURS', 48))
    RESET_TOKEN_HOURS = int(os.environ.get('RESET_TOKEN_HOURS', 2))

    # ─── Session Security ─────────────────────────────────────────────
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'false').lower() == 'true'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = os.environ.get('SESSION_COOKIE_SAMESITE', 'Lax')
    SESSION_LIFETIME_DAYS = int(os.environ.get('SESSION_LIFETIME_DAYS', 14))

    # ─── Error Monitoring (Sentry) ────────────────────────────────────
    SENTRY_DSN = os.environ.get('SENTRY_DSN', '')

    # ─── Content Moderation ────────────────────────────────────────────
    # Text moderation via OpenAI Moderation API (free)
    # Uses your OpenAI API key: https://platform.openai.com/api-keys
    MODERATION_ENABLED = os.environ.get('MODERATION_ENABLED', 'false').lower() == 'true'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')

    # Image moderation via AWS Rekognition (uses existing AWS creds)
    IMAGE_MODERATION_ENABLED = os.environ.get('IMAGE_MODERATION_ENABLED', 'false').lower() == 'true'

    @classmethod
    def get_db_type(cls):
        """Resolve the actual database type, accounting for DATABASE_URL."""
        if cls.DATABASE_URL:
            if cls.DATABASE_URL.startswith('postgres'):
                return 'postgres'
            elif cls.DATABASE_URL.startswith('mysql'):
                return 'mysql'
        return cls.DB_TYPE

    @classmethod
    def is_production(cls):
        return cls.get_db_type() in ('mysql', 'postgres')

    @classmethod
    def summary(cls):
        """Print config summary for startup."""
        db_type = cls.get_db_type()
        mode = 'PRODUCTION' if cls.is_production() else 'DEVELOPMENT'
        if db_type == 'postgres':
            db_info = f'postgres → {cls.POSTGRES_HOST}/{cls.POSTGRES_DATABASE}'
            if cls.DATABASE_URL:
                db_info = 'postgres → DATABASE_URL'
        elif db_type == 'mysql':
            db_info = f'mysql → {cls.MYSQL_HOST}/{cls.MYSQL_DATABASE}'
        else:
            db_info = f'sqlite → {cls.SQLITE_PATH}'
        lines = [
            f'  Mode:      {mode}',
            f'  Database:  {db_info}',
            f'  Storage:   {cls.STORAGE_TYPE}' + (f' → s3://{cls.AWS_S3_BUCKET}' if cls.STORAGE_TYPE == 's3' else ' → local'),
            f'  Email:     {cls.EMAIL_TYPE}' + (f' → Resend API' if cls.EMAIL_TYPE == 'resend' else f' → {cls.SMTP_HOST}' if cls.EMAIL_TYPE == 'smtp' else ' → console'),
            f'  Verify:    {"required" if cls.REQUIRE_EMAIL_VERIFICATION else "disabled"}',
            f'  Rate Limit: {"enabled" if cls.RATELIMIT_ENABLED else "disabled"}',
            f'  Sentry:    {"enabled" if cls.SENTRY_DSN else "disabled"}',
            f'  Moderation: {"enabled" if cls.MODERATION_ENABLED else "disabled"}',
            f'  Image Mod: {"enabled" if cls.IMAGE_MODERATION_ENABLED else "disabled"}',
        ]
        return '\n'.join(lines)
