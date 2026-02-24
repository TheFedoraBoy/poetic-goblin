"""
Poetic Goblin — Email Service
Supports console output (dev) and SMTP (prod).
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config


def send_email(to_email, subject, html_body, text_body=None):
    """
    Send an email.
    - Dev: prints to console
    - Prod: sends via SMTP
    """
    if Config.EMAIL_TYPE == 'smtp':
        return _send_smtp(to_email, subject, html_body, text_body)
    else:
        return _send_console(to_email, subject, html_body, text_body)


def _send_console(to_email, subject, html_body, text_body=None):
    """Print email to console (dev mode)."""
    print("\n" + "=" * 60)
    print(f"📧 EMAIL (console mode — not actually sent)")
    print(f"   To:      {to_email}")
    print(f"   Subject: {subject}")
    print(f"   Body:")
    print(f"   {text_body or html_body}")
    print("=" * 60 + "\n")
    return True


def _send_smtp(to_email, subject, html_body, text_body=None):
    """Send via SMTP."""
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = f"{Config.SMTP_FROM_NAME} <{Config.SMTP_FROM_EMAIL}>"
        msg['To'] = to_email

        if text_body:
            msg.attach(MIMEText(text_body, 'plain'))
        msg.attach(MIMEText(html_body, 'html'))

        if Config.SMTP_USE_TLS:
            server = smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT)
            server.ehlo()
            server.starttls()
        else:
            server = smtplib.SMTP_SSL(Config.SMTP_HOST, Config.SMTP_PORT)

        server.login(Config.SMTP_USER, Config.SMTP_PASSWORD)
        server.sendmail(Config.SMTP_FROM_EMAIL, to_email, msg.as_string())
        server.quit()
        return True

    except Exception as e:
        print(f"[Poetic Goblin] Email send failed: {e}")
        return False


# ─── Email Templates ──────────────────────────────────────────────────────────

def send_verification_email(to_email, username, token):
    """Send email verification link."""
    verify_url = f"{Config.BASE_URL}/verify/{token}"
    subject = "🧌 Verify your Poetic Goblin account"
    html = f"""
    <div style="font-family:sans-serif;max-width:500px;margin:0 auto;padding:2rem;">
        <h1 style="color:#1a73e8;">🧌 Welcome to Poetic Goblin!</h1>
        <p>Hey <strong>{username}</strong>,</p>
        <p>Click the button below to verify your email and enter the realm:</p>
        <div style="text-align:center;margin:2rem 0;">
            <a href="{verify_url}" style="display:inline-block;padding:0.75rem 2rem;background:#ff6b2b;color:white;text-decoration:none;border-radius:8px;font-weight:bold;font-size:1.1rem;">Verify My Email</a>
        </div>
        <p style="color:#666;font-size:0.85rem;">Or copy this link: {verify_url}</p>
        <p style="color:#666;font-size:0.85rem;">This link expires in {Config.VERIFICATION_TOKEN_HOURS} hours.</p>
        <hr style="border:none;border-top:1px solid #eee;margin:1.5rem 0;">
        <p style="color:#999;font-size:0.8rem;">If you didn't create this account, you can safely ignore this email.</p>
    </div>
    """
    text = f"Welcome to Poetic Goblin, {username}! Verify your email: {verify_url}"
    return send_email(to_email, subject, html, text)


def send_password_reset_email(to_email, username, token):
    """Send password reset link."""
    reset_url = f"{Config.BASE_URL}/reset-password/{token}"
    subject = "🧌 Reset your Poetic Goblin password"
    html = f"""
    <div style="font-family:sans-serif;max-width:500px;margin:0 auto;padding:2rem;">
        <h1 style="color:#1a73e8;">🧌 Password Reset</h1>
        <p>Hey <strong>{username}</strong>,</p>
        <p>Someone requested a password reset for your account. Click below to set a new password:</p>
        <div style="text-align:center;margin:2rem 0;">
            <a href="{reset_url}" style="display:inline-block;padding:0.75rem 2rem;background:#1a73e8;color:white;text-decoration:none;border-radius:8px;font-weight:bold;font-size:1.1rem;">Reset My Password</a>
        </div>
        <p style="color:#666;font-size:0.85rem;">Or copy this link: {reset_url}</p>
        <p style="color:#666;font-size:0.85rem;">This link expires in {Config.RESET_TOKEN_HOURS} hours.</p>
        <hr style="border:none;border-top:1px solid #eee;margin:1.5rem 0;">
        <p style="color:#999;font-size:0.8rem;">If you didn't request this, your account is safe — just ignore this email.</p>
    </div>
    """
    text = f"Reset your Poetic Goblin password: {reset_url} (expires in {Config.RESET_TOKEN_HOURS} hours)"
    return send_email(to_email, subject, html, text)
