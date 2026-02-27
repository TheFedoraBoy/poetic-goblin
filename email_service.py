"""
Poetic Goblin — Email Service
Supports: console (dev), SMTP (prod), Resend API (prod - recommended).

Set EMAIL_TYPE env var:
  - 'console' — prints to terminal (default, for dev)
  - 'smtp'    — sends via SMTP (Gmail, Postmark, Mailgun, etc.)
  - 'resend'  — sends via Resend HTTP API (recommended, simplest setup)
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config


def send_email(to_email, subject, html_body, text_body=None):
    """Send an email via the configured provider."""
    email_type = Config.EMAIL_TYPE
    if email_type == 'resend':
        return _send_resend(to_email, subject, html_body, text_body)
    elif email_type == 'smtp':
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


def _send_resend(to_email, subject, html_body, text_body=None):
    """Send via Resend HTTP API. Requires RESEND_API_KEY env var."""
    try:
        import urllib.request
        import urllib.error
        import json

        api_key = Config.RESEND_API_KEY
        if not api_key:
            print("[Poetic Goblin] RESEND_API_KEY not set. Falling back to console.")
            return _send_console(to_email, subject, html_body, text_body)

        payload = {
            "from": f"{Config.SMTP_FROM_NAME} <{Config.SMTP_FROM_EMAIL}>",
            "to": [to_email],
            "subject": subject,
            "html": html_body,
        }
        if text_body:
            payload["text"] = text_body

        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            'https://api.resend.com/emails',
            data=data,
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
                'User-Agent': 'PoeticGoblin/1.0',
            },
            method='POST',
        )

        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status in (200, 201):
                return True
            print(f"[Poetic Goblin] Resend API returned {resp.status}")
            return False

    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='replace')
        print(f"[Poetic Goblin] Resend email failed: HTTP {e.code} — {error_body}")
        return False
    except Exception as e:
        print(f"[Poetic Goblin] Resend email failed: {e}")
        return False


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
        print(f"[Poetic Goblin] SMTP email failed: {e}")
        return False


# ─── Email Templates ──────────────────────────────────────────────────────────

def send_verification_email(to_email, username, token):
    """Send email verification link."""
    verify_url = f"{Config.BASE_URL}/verify/{token}"
    subject = "Verify your Poetic Goblin account"
    html = f"""
    <div style="font-family:sans-serif;max-width:500px;margin:0 auto;padding:2rem;background:#fafaf7;border-radius:12px;">
        <div style="text-align:center;margin-bottom:1.5rem;">
            <span style="font-size:2.5rem;">🧌</span>
        </div>
        <h1 style="color:#1a3a5c;text-align:center;margin-bottom:0.5rem;">Welcome to Poetic Goblin!</h1>
        <p style="text-align:center;color:#666;">Hey <strong>{username}</strong>, verify your email to enter the realm.</p>
        <div style="text-align:center;margin:2rem 0;">
            <a href="{verify_url}" style="display:inline-block;padding:0.75rem 2rem;background:#ff6b2b;color:white;text-decoration:none;border-radius:8px;font-weight:bold;font-size:1.1rem;">Verify My Email</a>
        </div>
        <p style="color:#999;font-size:0.82rem;text-align:center;">Or copy: {verify_url}</p>
        <p style="color:#999;font-size:0.82rem;text-align:center;">Expires in {Config.VERIFICATION_TOKEN_HOURS} hours.</p>
        <hr style="border:none;border-top:1px solid #e0e0e0;margin:1.5rem 0;">
        <p style="color:#bbb;font-size:0.78rem;text-align:center;">If you didn't create this account, ignore this email.</p>
    </div>
    """
    text = f"Welcome to Poetic Goblin, {username}! Verify your email: {verify_url}"
    return send_email(to_email, subject, html, text)


def send_welcome_email(to_email, username):
    """Send a welcome email explaining what Poetic Goblin is and what you can do."""
    feed_url = f"{Config.BASE_URL}/feed"
    character_url = f"{Config.BASE_URL}/character/create"
    annals_url = f"{Config.BASE_URL}/annals"
    subject = "Welcome to Poetic Goblin — your adventure begins! 🧌"
    html = f"""
    <div style="font-family:sans-serif;max-width:560px;margin:0 auto;padding:2rem;background:#fafaf7;border-radius:12px;">
        <div style="text-align:center;margin-bottom:1.5rem;">
            <span style="font-size:2.5rem;">🧌</span>
        </div>
        <h1 style="color:#1a3a5c;text-align:center;margin-bottom:0.5rem;">Welcome to Poetic Goblin!</h1>
        <p style="text-align:center;color:#666;margin-bottom:1.5rem;">Hey <strong>{username}</strong>, we're thrilled to have you in the realm.</p>

        <p style="color:#333;line-height:1.7;">
            Poetic Goblin is a social platform built for D&amp;D fans and fantasy lovers.
            It's a place to share stories, showcase art, log campaigns, and connect with
            fellow adventurers — all through the lens of your characters.
        </p>

        <h2 style="color:#1a3a5c;font-size:1.1rem;margin-top:1.5rem;">Here's what you can do:</h2>

        <table style="width:100%;border-collapse:collapse;margin:1rem 0;">
            <tr>
                <td style="padding:0.6rem 0.8rem;vertical-align:top;font-size:1.3rem;">⚔️</td>
                <td style="padding:0.6rem 0.8rem;color:#333;">
                    <strong>Create characters</strong> — Build your adventurers with races, classes,
                    traits, backstories, and avatars. Switch between them any time.
                </td>
            </tr>
            <tr>
                <td style="padding:0.6rem 0.8rem;vertical-align:top;font-size:1.3rem;">📜</td>
                <td style="padding:0.6rem 0.8rem;color:#333;">
                    <strong>Share stories &amp; art</strong> — Post tales from your campaigns,
                    share character art, maps, and tag them with locations and ages from
                    the World of Elysal.
                </td>
            </tr>
            <tr>
                <td style="padding:0.6rem 0.8rem;vertical-align:top;font-size:1.3rem;">🗡️</td>
                <td style="padding:0.6rem 0.8rem;color:#333;">
                    <strong>Log campaigns</strong> — Record your sessions with multi-part
                    campaign logs so your party's journey is never forgotten.
                </td>
            </tr>
            <tr>
                <td style="padding:0.6rem 0.8rem;vertical-align:top;font-size:1.3rem;">📖</td>
                <td style="padding:0.6rem 0.8rem;color:#333;">
                    <strong>Explore the Annals of Elysal</strong> — Read the shared lore of our
                    fantasy world and contribute your own stories to its history.
                </td>
            </tr>
            <tr>
                <td style="padding:0.6rem 0.8rem;vertical-align:top;font-size:1.3rem;">💬</td>
                <td style="padding:0.6rem 0.8rem;color:#333;">
                    <strong>Connect</strong> — Follow other adventurers, comment on posts,
                    and send direct messages to plan your next quest.
                </td>
            </tr>
        </table>

        <h2 style="color:#1a3a5c;font-size:1.1rem;margin-top:1.5rem;">Getting started:</h2>
        <p style="color:#333;line-height:1.7;">
            Your first step is to <a href="{character_url}" style="color:#ff6b2b;font-weight:600;">forge a character</a>.
            Once you do, you'll unlock the <a href="{feed_url}" style="color:#ff6b2b;font-weight:600;">feed</a>,
            the <a href="{annals_url}" style="color:#ff6b2b;font-weight:600;">Annals</a>, and everything else
            the realm has to offer.
        </p>

        <div style="text-align:center;margin:2rem 0;">
            <a href="{character_url}" style="display:inline-block;padding:0.75rem 2rem;background:#ff6b2b;color:white;text-decoration:none;border-radius:8px;font-weight:bold;font-size:1.1rem;">Create Your Character</a>
        </div>

        <hr style="border:none;border-top:1px solid #e0e0e0;margin:1.5rem 0;">
        <p style="color:#bbb;font-size:0.78rem;text-align:center;">
            You're receiving this because you signed up at Poetic Goblin. Happy adventuring!
        </p>
    </div>
    """
    text = (
        f"Welcome to Poetic Goblin, {username}!\n\n"
        "Poetic Goblin is a social platform for D&D fans and fantasy lovers. "
        "Share stories, showcase art, log campaigns, and connect with fellow adventurers.\n\n"
        "What you can do:\n"
        "- Create characters with races, classes, traits, and backstories\n"
        "- Share stories, art, and maps tagged with World of Elysal lore\n"
        "- Log multi-session campaigns\n"
        "- Explore and contribute to the Annals of Elysal\n"
        "- Follow adventurers, comment, and send direct messages\n\n"
        f"Get started by creating your first character: {character_url}\n\n"
        "Happy adventuring!"
    )
    return send_email(to_email, subject, html, text)


def send_password_reset_email(to_email, username, token):
    """Send password reset link."""
    reset_url = f"{Config.BASE_URL}/reset-password/{token}"
    subject = "Reset your Poetic Goblin password"
    html = f"""
    <div style="font-family:sans-serif;max-width:500px;margin:0 auto;padding:2rem;background:#fafaf7;border-radius:12px;">
        <div style="text-align:center;margin-bottom:1.5rem;">
            <span style="font-size:2.5rem;">🧌</span>
        </div>
        <h1 style="color:#1a3a5c;text-align:center;margin-bottom:0.5rem;">Password Reset</h1>
        <p style="text-align:center;color:#666;">Hey <strong>{username}</strong>, click below to set a new password.</p>
        <div style="text-align:center;margin:2rem 0;">
            <a href="{reset_url}" style="display:inline-block;padding:0.75rem 2rem;background:#1a73e8;color:white;text-decoration:none;border-radius:8px;font-weight:bold;font-size:1.1rem;">Reset My Password</a>
        </div>
        <p style="color:#999;font-size:0.82rem;text-align:center;">Or copy: {reset_url}</p>
        <p style="color:#999;font-size:0.82rem;text-align:center;">Expires in {Config.RESET_TOKEN_HOURS} hours.</p>
        <hr style="border:none;border-top:1px solid #e0e0e0;margin:1.5rem 0;">
        <p style="color:#bbb;font-size:0.78rem;text-align:center;">If you didn't request this, your account is safe — ignore this email.</p>
    </div>
    """
    text = f"Reset your Poetic Goblin password: {reset_url} (expires in {Config.RESET_TOKEN_HOURS} hours)"
    return send_email(to_email, subject, html, text)
