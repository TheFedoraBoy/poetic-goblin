"""
Poetic Goblin - A Social Media for D&D Fans and Fantasy Enjoyers
Flask Application — Production-Ready with MySQL/PostgreSQL, S3, SMTP, Rate Limiting
"""

import os
import re
import uuid
import json
import secrets
import hmac
import hashlib
from datetime import datetime, timedelta
from functools import wraps

from flask import (
    Flask, render_template, request, redirect, url_for,
    flash, session, jsonify, g, abort
)
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from database import get_db, close_db, init_db
from storage import save_upload, allowed_file
from email_service import send_verification_email, send_password_reset_email
from annals_data import AGES as ANNALS_AGES, ANNALS_INTRO

# ─── Sentry Error Monitoring ─────────────────────────────────────────────────

if Config.SENTRY_DSN:
    try:
        import sentry_sdk
        from sentry_sdk.integrations.flask import FlaskIntegration
        sentry_sdk.init(
            dsn=Config.SENTRY_DSN,
            integrations=[FlaskIntegration()],
            traces_sample_rate=0.1,
            send_default_pii=False,
        )
        print("[Poetic Goblin] Sentry error monitoring enabled.")
    except ImportError:
        print("[Poetic Goblin] sentry-sdk not installed. Error monitoring disabled.")

SENTRY_TEST_ENABLED = False  # Set to True temporarily to test Sentry

# ─── App Configuration ────────────────────────────────────────────────────────

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

# Session security
app.config['SESSION_COOKIE_SECURE'] = Config.SESSION_COOKIE_SECURE
app.config['SESSION_COOKIE_HTTPONLY'] = Config.SESSION_COOKIE_HTTPONLY
app.config['SESSION_COOKIE_SAMESITE'] = Config.SESSION_COOKIE_SAMESITE

# Register teardown
app.teardown_appcontext(close_db)

# ─── CSRF Protection ─────────────────────────────────────────────────────────

def generate_csrf_token():
    """Generate a CSRF token and store it in the session."""
    if '_csrf_token' not in session:
        session['_csrf_token'] = secrets.token_hex(32)
    return session['_csrf_token']

def validate_csrf_token():
    """Validate the CSRF token from the request."""
    token = request.form.get('_csrf_token') or request.headers.get('X-CSRF-Token')
    if not token or token != session.get('_csrf_token'):
        abort(403)

@app.before_request
def csrf_protect():
    """Check CSRF token on all POST/PUT/DELETE requests."""
    if request.method in ('POST', 'PUT', 'DELETE'):
        # AJAX requests: validate via X-CSRF-Token header
        if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            token = request.headers.get('X-CSRF-Token')
            if not token or token != session.get('_csrf_token'):
                abort(403)
            return
        validate_csrf_token()

@app.context_processor
def inject_csrf():
    """Make csrf_token() available in all templates."""
    return dict(csrf_token=generate_csrf_token)

# ─── Security Headers ────────────────────────────────────────────────────────

@app.after_request
def set_security_headers(response):
    """Add security headers to all responses."""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'

    # Build dynamic img-src based on storage config
    img_sources = "'self' data:"
    if Config.AWS_S3_CUSTOM_DOMAIN:
        img_sources += f" https://{Config.AWS_S3_CUSTOM_DOMAIN}"
    elif Config.AWS_S3_BUCKET:
        img_sources += f" https://{Config.AWS_S3_BUCKET}.s3.{Config.AWS_S3_REGION}.amazonaws.com"
    if Config.AWS_S3_ENDPOINT_URL:
        img_sources += f" {Config.AWS_S3_ENDPOINT_URL}"
    # Always allow amazonaws.com as fallback
    img_sources += " https://*.amazonaws.com"

    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        f"img-src {img_sources}; "
        "font-src 'self' https://fonts.gstatic.com; "
        "frame-ancestors 'none'"
    )
    if Config.SESSION_COOKIE_SECURE:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

# ─── Error Handlers ──────────────────────────────────────────────────────────

@app.errorhandler(403)
def forbidden_error(e):
    return render_template('error.html', code=403, title='Forbidden',
        message='Your session may have expired. Try refreshing the page or logging in again.'), 403

@app.errorhandler(404)
def not_found_error(e):
    return render_template('error.html', code=404, title='Page Not Found',
        message='This path leads nowhere. The page you seek does not exist in this realm.'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', code=500, title='Something Went Wrong',
        message='A dark spell has disrupted the realm. Our wizards have been notified.'), 500

@app.errorhandler(413)
def too_large_error(e):
    return render_template('error.html', code=413, title='File Too Large',
        message='Your upload exceeds the maximum size allowed. Try a smaller file.'), 413

# Temporary test route — remove after confirming Sentry works
if SENTRY_TEST_ENABLED:
    @app.route('/sentry-test')
    def sentry_test():
        raise Exception("Sentry test — this error is intentional! Delete the /sentry-test route from app.py.")

# ─── Rate Limiting ────────────────────────────────────────────────────────────

try:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["200 per hour", "50 per minute"],
        storage_uri=Config.RATELIMIT_STORAGE_URI,
        enabled=Config.RATELIMIT_ENABLED,
    )
except ImportError:
    print("[Poetic Goblin] flask-limiter not installed. Rate limiting disabled.")
    class _NoOpLimiter:
        def limit(self, *a, **kw):
            def decorator(f): return f
            return decorator
        def exempt(self, f): return f
    limiter = _NoOpLimiter()

# ─── 100 Character Traits ────────────────────────────────────────────────────

CHARACTER_TRAITS = [
    "Fearless","Ruthless","Relentless","Savage","Ironwilled",
    "Berserker","Unyielding","Brutal","Warborn","Bloodthirsty",
    "Strategic","Cunning","Analytical","Perceptive","Calculating",
    "Resourceful","Inventive","Scholarly","Visionary","Meticulous",
    "Charismatic","Eloquent","Persuasive","Inspiring","Commanding",
    "Diplomatic","Charming","Silver-Tongued","Regal","Magnetic",
    "Compassionate","Generous","Selfless","Nurturing","Empathetic",
    "Forgiving","Gentle","Kindhearted","Merciful","Charitable",
    "Deceptive","Manipulative","Vengeful","Paranoid","Obsessive",
    "Jealous","Wrathful","Greedy","Vain","Treacherous",
    "Stealthy","Elusive","Sly","Quick-Witted","Shadowy",
    "Nimble","Silent","Devious","Daring","Unpredictable",
    "Wise","Mystical","Prophetic","Serene","Enigmatic",
    "Ancient-Souled","Ethereal","Meditative","Otherworldly","Farsighted",
    "Honorable","Loyal","Dutiful","Righteous","Just",
    "Stalwart","Oathbound","Noble","Devoted","Chivalrous",
    "Feral","Primal","Untamed","Nature-Bound","Beastlike",
    "Nomadic","Earthen","Stormblooded","Wildborn","Elemental",
    "Eccentric","Whimsical","Sardonic","Melancholic","Theatrical",
    "Rebellious","Haunted","Brooding","Jovial","Fatalistic",
]

# ─── World of Elysal ─────────────────────────────────────────────────────────

ELYSAL_LOCATIONS = [
    "The Shattered Coast", "Valdris, City of Tides", "The Silver Tower",
    "Thornwood Forest", "Duskhollow", "Kragmore Arena",
    "The Whispering Grove", "Frostspire Mountains", "The Verdant Expanse",
    "Embervault Citadel", "The Sunken Bazaar", "Moonlit Court",
    "The Iron Wastes", "Stormreach Harbour", "The Hollowed Catacombs",
    "Ashenmoor Swamps", "Crystalpeak Monastery", "The Wandering Isles",
    "Blackthorn Keep", "The Gilded Undercity", "Starfall Ruins",
    "The Crimson Sands", "Eldergrove Sanctuary", "Dragonmaw Pass",
    "The Feywild Crossing", "Shadowfell Gate", "Abyssal Rift",
    "The Celestial Spire", "Misthollow Caverns", "The Eternal Bazaar",
]

ELYSAL_AGES = [
    "The Age of First Light", "The Year of Shattered Crowns",
    "The Age of Long Knives", "The Year of Snow",
    "The Age of Burning Seas", "The Dragonfall Era",
    "The Year of Whispered Oaths", "The Age of Iron and Ash",
    "The Sundering", "The Year of the Crimson Moon",
    "The Age of the Silver Compact", "The Year of Hollow Thrones",
    "The Age of Wandering Stars", "The Blight Years",
    "The Age of the Verdant Bloom", "The Year of the Last Dragon",
    "The Age of Tides", "The Year of Broken Chains",
    "The Age of Echoes", "The Current Age — The Reckoning",
]

ELYSAL_CHARACTERS = [
    {"name": "Vaelith the Undying", "desc": "Ancient lich who seeks redemption"},
    {"name": "Queen Seraphine", "desc": "Ruler of Valdris, master diplomat"},
    {"name": "Thorn", "desc": "Mysterious ranger of the Thornwood"},
    {"name": "Malachar the Red", "desc": "Dragon warlord of the Crimson Sands"},
    {"name": "Sister Avarice", "desc": "High priestess with dark motives"},
    {"name": "Fenwick Cogsworth", "desc": "Gnome inventor, slightly unhinged"},
    {"name": "The Hollow King", "desc": "Undead ruler of the Hollowed Catacombs"},
    {"name": "Lyssa Dawnstrider", "desc": "Paladin of the Celestial Spire"},
    {"name": "Rattleclaw", "desc": "Goblin merchant prince of the Sunken Bazaar"},
    {"name": "Orin Stormweaver", "desc": "Half-giant sorcerer of the Iron Wastes"},
    {"name": "The Pale Dancer", "desc": "Fey spirit who grants dangerous wishes"},
    {"name": "Captain Blacktide", "desc": "Pirate lord of the Shattered Coast"},
    {"name": "Yennifer of Moonlit Court", "desc": "Tiefling bard and spymaster"},
    {"name": "Elder Mossbeard", "desc": "Ancient treant guardian of Eldergrove"},
    {"name": "Krix the Unbroken", "desc": "Orc gladiator champion of Kragmore"},
]

PRESET_AVATARS = [
    {"file": "/static/avatars/avatar_warrior.svg", "label": "Warrior"},
    {"file": "/static/avatars/avatar_mage.svg", "label": "Mage"},
    {"file": "/static/avatars/avatar_rogue.svg", "label": "Rogue"},
    {"file": "/static/avatars/avatar_elf.svg", "label": "Elf"},
    {"file": "/static/avatars/avatar_dwarf.svg", "label": "Pkoyte"},
    {"file": "/static/avatars/avatar_orc.svg", "label": "Orc"},
    {"file": "/static/avatars/avatar_necromancer.svg", "label": "Necromancer"},
    {"file": "/static/avatars/avatar_ranger.svg", "label": "Ranger"},
    {"file": "/static/avatars/avatar_cleric.svg", "label": "Cleric"},
    {"file": "/static/avatars/avatar_tiefling.svg", "label": "Karagonian"},
    {"file": "/static/avatars/avatar_dragonborn.svg", "label": "Dragonborn"},
    {"file": "/static/avatars/avatar_bard.svg", "label": "Bard"},
    {"file": "/static/avatars/avatar_paladin.svg", "label": "Paladin"},
    {"file": "/static/avatars/avatar_warlock.svg", "label": "Warlock"},
    {"file": "/static/avatars/avatar_sorcerer.svg", "label": "Sorcerer"},
    {"file": "/static/avatars/avatar_monk.svg", "label": "Monk"},
    {"file": "/static/avatars/avatar_druid.svg", "label": "Druid"},
    {"file": "/static/avatars/avatar_halfling.svg", "label": "Hiyalmite"},
    {"file": "/static/avatars/avatar_lizardfolk.svg", "label": "Lirzan"},
    {"file": "/static/avatars/avatar_winterman.svg", "label": "Winterman"},
    {"file": "/static/avatars/avatar_pridekin.svg", "label": "Pridekin"},
    {"file": "/static/avatars/avatar_dark_knight.svg", "label": "Dark Knight"},
    {"file": "/static/avatars/avatar_barbarian.svg", "label": "Barbarian"},
    {"file": "/static/avatars/avatar_alchemist.svg", "label": "Alchemist"},
    {"file": "/static/avatars/avatar_pirate.svg", "label": "Pirate"},
    {"file": "/static/avatars/avatar_scholar.svg", "label": "Scholar"},
    {"file": "/static/avatars/avatar_shaman.svg", "label": "Shaman"},
    {"file": "/static/avatars/avatar_assassin.svg", "label": "Assassin"},
    {"file": "/static/avatars/avatar_knight.svg", "label": "Knight"},
    {"file": "/static/avatars/avatar_mystic.svg", "label": "Mystic"},
]

CHARACTER_RACES = ['Human', 'Elf', 'Pkoyte', 'Hiyalmite', 'Karagonian', 'Lirzan', 'Winterman', 'Pridekin']
CHARACTER_RACE_LABELS = {
    'Human': 'Human',
    'Elf': 'Elf',
    'Pkoyte': 'Pkoyte (Dwarf)',
    'Hiyalmite': 'Hiyalmite (Halfling)',
    'Karagonian': 'Karagonian (Tiefling)',
    'Lirzan': 'Lirzan (Lizardfolk)',
    'Winterman': 'Winterman',
    'Pridekin': 'Pridekin',
}
CHARACTER_CLASSES = ['Warrior', 'Rogue', 'Ranger', 'Paladin', 'Cleric', 'Wizard', 'Warlock', 'Sorcerer', 'Monk', 'Druid', 'Bard']

# ─── Auth Helpers ─────────────────────────────────────────────────────

def validate_password(password):
    """Validate password strength. Returns list of error messages (empty = valid)."""
    errors = []
    if len(password) < 8:
        errors.append('Password must be at least 8 characters.')
    if not any(c.isdigit() for c in password):
        errors.append('Password must contain at least one number.')
    if not any(c.isalpha() for c in password):
        errors.append('Password must contain at least one letter.')
    return errors

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('You must be logged in.', 'warning')
            return redirect(url_for('login'))
        db = get_db()
        try:
            user = db.fetchone('SELECT id FROM users WHERE id = %s', (session['user_id'],))
            if not user:
                session.clear()
                flash('Session expired. Please log in again.', 'warning')
                return redirect(url_for('login'))
        except Exception:
            session.clear()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def character_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        db = get_db()
        try:
            user = db.fetchone('SELECT id FROM users WHERE id = %s', (session['user_id'],))
            if not user:
                session.clear()
                flash('Session expired. Please log in again.', 'warning')
                return redirect(url_for('login'))
            if not db.fetchone('SELECT id FROM characters WHERE user_id = %s LIMIT 1',
                               (session['user_id'],)):
                flash('Create a character first!', 'warning')
                return redirect(url_for('create_character'))
        except Exception:
            session.clear()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def get_current_user():
    if 'user_id' in session:
        db = get_db()
        try:
            user = db.fetchone('''
                SELECT u.id, u.username, u.email, u.joined_at,
                       c.id as char_id, c.name as char_name, c.trait1, c.trait2, c.trait3,
                       c.backstory, c.avatar_url as char_avatar
                FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
                WHERE u.id = %s
            ''', (session['user_id'],))
            if user:
                return user
            session.clear()
        except Exception:
            session.clear()
    return None

@app.context_processor
def inject_globals():
    unread_count = 0
    user = None
    if 'user_id' in session:
        user = get_current_user()
        if user:
            try:
                db = get_db()
                row = db.fetchone('''
                    SELECT COUNT(*) as c FROM messages m
                    JOIN conversations cv ON m.conversation_id = cv.id
                    WHERE (cv.user1_id = %s OR cv.user2_id = %s) AND m.sender_id != %s AND m.is_read = 0
                ''', (session['user_id'], session['user_id'], session['user_id']))
                unread_count = row['c'] if row else 0
            except Exception:
                pass
    return dict(
        current_user=user,
        elysal_locations=ELYSAL_LOCATIONS,
        elysal_ages=ELYSAL_AGES,
        elysal_characters=ELYSAL_CHARACTERS,
        annals_ages=ANNALS_AGES,
        unread_message_count=unread_count,
    )

@app.template_filter('timeago')
def timeago_filter(dt_string):
    try:
        if isinstance(dt_string, datetime):
            dt = dt_string
        else:
            dt = datetime.strptime(str(dt_string), '%Y-%m-%d %H:%M:%S')
    except (ValueError, TypeError):
        return str(dt_string)
    diff = (datetime.now() - dt).total_seconds()
    if diff < 60: return 'just now'
    if diff < 3600: return f'{int(diff/60)}m ago'
    if diff < 86400: return f'{int(diff/3600)}h ago'
    if diff < 604800: return f'{int(diff/86400)}d ago'
    return dt.strftime('%b %d, %Y')

# ─── Routes: Auth ─────────────────────────────────────────────────────────────

@app.route('/')
def index():
    if 'user_id' in session:
        db = get_db()
        try:
            user = db.fetchone('SELECT id FROM users WHERE id = %s', (session['user_id'],))
            if user:
                return redirect(url_for('feed'))
        except Exception:
            pass
        session.clear()
    return render_template('landing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy')
def privacy_policy():
    return render_template('privacy.html', last_updated='February 2026')

@app.route('/terms')
def terms_of_service():
    return render_template('terms.html', last_updated='February 2026')

@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')
        errors = []
        if len(username) < 3 or len(username) > 30: errors.append('Username must be 3-30 characters.')
        if not re.match(r'^[a-zA-Z0-9_-]+$', username): errors.append('Username can only contain letters, numbers, hyphens, and underscores.')
        if not email or '@' not in email: errors.append('Valid email required.')
        pw_errors = validate_password(password)
        if pw_errors: errors.extend(pw_errors)
        if password != confirm: errors.append('Passwords do not match.')
        db = get_db()
        if db.fetchone('SELECT id FROM users WHERE username = %s', (username,)):
            errors.append('Registration failed — username or email may already be in use.')
        elif db.fetchone('SELECT id FROM users WHERE email = %s', (email,)):
            errors.append('Registration failed — username or email may already be in use.')
        if errors:
            for e in errors: flash(e, 'error')
            return render_template('register.html', username=username, email=email)
        user_id = str(uuid.uuid4())
        verification_token = secrets.token_urlsafe(32)
        db.execute(
            'INSERT INTO users (id, username, email, password_hash, email_verified, verification_token) VALUES (%s,%s,%s,%s,%s,%s)',
            (user_id, username, email, generate_password_hash(password),
             0 if Config.REQUIRE_EMAIL_VERIFICATION else 1,
             verification_token if Config.REQUIRE_EMAIL_VERIFICATION else ''))
        if Config.REQUIRE_EMAIL_VERIFICATION:
            send_verification_email(email, username, verification_token)
            flash('Account created! Check your email to verify.', 'success')
            return redirect(url_for('login'))
        else:
            session['user_id'] = user_id
            flash('Account created! Now forge your first character.', 'success')
            return redirect(url_for('create_character'))
    return render_template('register.html')

@app.route('/verify/<token>')
def verify_email(token):
    db = get_db()
    user = db.fetchone('SELECT id, username, joined_at FROM users WHERE verification_token = %s AND email_verified = 0', (token,))
    if not user:
        flash('Invalid or expired verification link.', 'error')
        return redirect(url_for('login'))
    # Check token hasn't expired (based on join time + configured hours)
    try:
        joined = user['joined_at']
        if isinstance(joined, str):
            joined = datetime.strptime(joined, '%Y-%m-%d %H:%M:%S')
        if datetime.now() - joined > timedelta(hours=Config.VERIFICATION_TOKEN_HOURS):
            flash('Verification link has expired. Please register again.', 'error')
            return redirect(url_for('register'))
    except (ValueError, TypeError):
        pass
    db.execute("UPDATE users SET email_verified = 1, verification_token = '' WHERE id = %s", (user['id'],))
    flash('Email verified! Welcome, {}. You may now log in.'.format(user['username']), 'success')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("20 per hour")
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        db = get_db()
        user = db.fetchone('SELECT id, username, password_hash, email_verified FROM users WHERE username = %s', (username,))
        if user and check_password_hash(user['password_hash'], password):
            if Config.REQUIRE_EMAIL_VERIFICATION and not user['email_verified']:
                flash('Please verify your email first. Check your inbox, or click below to resend.', 'warning')
                return render_template('login.html', show_resend=True, resend_username=username)
            session.clear()
            session['user_id'] = user['id']
            if not db.fetchone('SELECT id FROM characters WHERE user_id = %s', (user['id'],)):
                return redirect(url_for('create_character'))
            flash('Welcome back!', 'success')
            return redirect(url_for('feed'))
        flash('Invalid credentials.', 'error')
    return render_template('login.html')

@app.route('/resend-verification', methods=['POST'])
@limiter.limit("5 per hour")
def resend_verification():
    username = request.form.get('username', '').strip()
    db = get_db()
    user = db.fetchone('SELECT id, username, email, email_verified, verification_token FROM users WHERE username = %s', (username,))
    if user and not user['email_verified']:
        token = user['verification_token']
        if not token:
            token = secrets.token_urlsafe(32)
            db.execute('UPDATE users SET verification_token = %s WHERE id = %s', (token, user['id']))
        send_verification_email(user['email'], user['username'], token)
    # Always show success to prevent enumeration
    flash('If that account exists, a verification email has been sent.', 'success')
    return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.clear()
    flash('Logged out. Safe travels!', 'info')
    return redirect(url_for('index'))

# ─── Routes: Password Reset ──────────────────────────────────────────────────

@app.route('/forgot-password', methods=['GET', 'POST'])
@limiter.limit("5 per hour")
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        db = get_db()
        user = db.fetchone('SELECT id, username, email FROM users WHERE email = %s', (email,))
        if user:
            token = secrets.token_urlsafe(32)
            expires = datetime.now() + timedelta(hours=Config.RESET_TOKEN_HOURS)
            db.execute('UPDATE users SET reset_token = %s, reset_token_expires = %s WHERE id = %s',
                       (token, expires.strftime('%Y-%m-%d %H:%M:%S'), user['id']))
            send_password_reset_email(user['email'], user['username'], token)
        flash('If that email exists, a reset link has been sent.', 'info')
        return redirect(url_for('login'))
    return render_template('forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
def reset_password(token):
    db = get_db()
    user = db.fetchone(
        'SELECT id, username FROM users WHERE reset_token = %s AND reset_token_expires > %s',
        (token, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    if not user:
        flash('Invalid or expired reset link.', 'error')
        return redirect(url_for('forgot_password'))
    if request.method == 'POST':
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')
        pw_errors = validate_password(password)
        if pw_errors:
            for e in pw_errors: flash(e, 'error')
            return render_template('reset_password.html', token=token)
        if password != confirm:
            flash('Passwords do not match.', 'error')
            return render_template('reset_password.html', token=token)
        db.execute("UPDATE users SET password_hash = %s, reset_token = '', reset_token_expires = NULL WHERE id = %s",
                   (generate_password_hash(password), user['id']))
        flash('Password reset! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', token=token)

# ─── Routes: Account Settings ────────────────────────────────────────────────

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    db = get_db()
    user = db.fetchone('SELECT id, username, email, email_verified, joined_at FROM users WHERE id = %s', (session['user_id'],))
    if not user:
        session.clear()
        return redirect(url_for('login'))
    if request.method == 'POST':
        action = request.form.get('action', '')
        if action == 'change_email':
            new_email = request.form.get('email', '').strip().lower()
            if not new_email or '@' not in new_email:
                flash('Valid email required.', 'error')
            elif db.fetchone('SELECT id FROM users WHERE email = %s AND id != %s', (new_email, user['id'])):
                flash('Email already in use.', 'error')
            else:
                if Config.REQUIRE_EMAIL_VERIFICATION:
                    # Set new email but mark as unverified, send verification
                    token = secrets.token_urlsafe(32)
                    db.execute('UPDATE users SET email = %s, email_verified = 0, verification_token = %s WHERE id = %s',
                               (new_email, token, user['id']))
                    send_verification_email(new_email, user['username'], token)
                    flash('Email updated! Please check your new inbox to re-verify.', 'success')
                else:
                    db.execute('UPDATE users SET email = %s WHERE id = %s', (new_email, user['id']))
                    flash('Email updated!', 'success')
        elif action == 'change_password':
            current = request.form.get('current_password', '')
            new_pw = request.form.get('new_password', '')
            confirm = request.form.get('confirm_password', '')
            if not check_password_hash(user['password_hash'], current):
                flash('Current password is incorrect.', 'error')
            else:
                pw_errors = validate_password(new_pw)
                if pw_errors:
                    for e in pw_errors: flash(e, 'error')
                elif new_pw != confirm:
                    flash('Passwords do not match.', 'error')
                else:
                    db.execute('UPDATE users SET password_hash = %s WHERE id = %s',
                               (generate_password_hash(new_pw), user['id']))
                    flash('Password changed!', 'success')
        return redirect(url_for('account_settings'))
    return render_template('settings.html', user=user)

@app.route('/settings/delete-account', methods=['POST'])
@login_required
def delete_account():
    db = get_db()
    password = request.form.get('password', '')
    user = db.fetchone('SELECT id, password_hash FROM users WHERE id = %s', (session['user_id'],))
    if not user or not check_password_hash(user['password_hash'], password):
        flash('Incorrect password. Account not deleted.', 'error')
        return redirect(url_for('account_settings'))
    uid = user['id']
    db.execute('DELETE FROM annals_stories WHERE author_id = %s', (uid,))
    db.execute('DELETE FROM messages WHERE sender_id = %s', (uid,))
    db.execute('DELETE FROM conversations WHERE user1_id = %s OR user2_id = %s', (uid, uid))
    db.execute('DELETE FROM comments WHERE author_id = %s', (uid,))
    db.execute('DELETE FROM likes WHERE user_id = %s', (uid,))
    db.execute('DELETE FROM follows WHERE follower_id = %s OR followed_id = %s', (uid, uid))
    db.execute('DELETE FROM campaign_sessions WHERE post_id IN (SELECT id FROM posts WHERE author_id = %s)', (uid,))
    db.execute('DELETE FROM posts WHERE author_id = %s', (uid,))
    db.execute('DELETE FROM characters WHERE user_id = %s', (uid,))
    db.execute('DELETE FROM users WHERE id = %s', (uid,))
    session.clear()
    flash('Your account has been deleted. Farewell, adventurer.', 'info')
    return redirect(url_for('index'))

# ─── Routes: Character ───────────────────────────────────────────────────────

@app.route('/character/create', methods=['GET', 'POST'])
@login_required
def create_character():
    if request.method == 'POST':
        char_name = request.form.get('char_name', '').strip()
        char_race = request.form.get('char_race', '')
        char_class = request.form.get('char_class', '')
        trait1 = request.form.get('trait1', '')
        trait2 = request.form.get('trait2', '')
        trait3 = request.form.get('trait3', '')
        backstory = request.form.get('backstory', '').strip()
        errors = []
        if len(char_name) < 2: errors.append('Name must be 2+ characters.')
        if char_race not in CHARACTER_RACES: errors.append('Please select a race.')
        if char_class not in CHARACTER_CLASSES: errors.append('Please select a class.')
        selected = [t for t in [trait1, trait2, trait3] if t]
        if len(selected) < 3: errors.append('Select exactly 3 traits.')
        if len(backstory) < 20: errors.append('Backstory must be 20+ characters.')
        if errors:
            for e in errors: flash(e, 'error')
            return render_template('create_character.html', traits=CHARACTER_TRAITS,
                                   char_name=char_name, char_race=char_race, char_class=char_class,
                                   trait1=trait1, trait2=trait2, trait3=trait3, backstory=backstory,
                                   preset_avatars=PRESET_AVATARS, races=CHARACTER_RACES,
                                   race_labels=CHARACTER_RACE_LABELS, classes=CHARACTER_CLASSES)
        db = get_db()
        avatar_url = ''
        preset = request.form.get('preset_avatar', '')
        valid_presets = [a['file'] for a in PRESET_AVATARS]
        if preset and preset in valid_presets:
            avatar_url = preset
        elif 'avatar' in request.files and request.files['avatar'].filename:
            avatar_url = save_upload(request.files['avatar'], 'avatars')
        existing = db.fetchone('SELECT COUNT(*) as c FROM characters WHERE user_id = %s', (session['user_id'],))
        is_main = 1 if (not existing or existing['c'] == 0) else 0
        char_id = str(uuid.uuid4())
        db.execute('INSERT INTO characters (id,user_id,name,race,class,trait1,trait2,trait3,backstory,avatar_url,is_main) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                   (char_id, session['user_id'], char_name, char_race, char_class, trait1, trait2, trait3, backstory, avatar_url, is_main))
        if is_main:
            db.execute('UPDATE users SET main_character_id = %s WHERE id = %s', (char_id, session['user_id']))
        flash('{} has entered the realm!'.format(char_name), 'success')
        return redirect(url_for('feed'))
    return render_template('create_character.html', traits=CHARACTER_TRAITS,
                           char_name='', char_race='', char_class='',
                           trait1='', trait2='', trait3='', backstory='',
                           preset_avatars=PRESET_AVATARS, races=CHARACTER_RACES,
                           race_labels=CHARACTER_RACE_LABELS, classes=CHARACTER_CLASSES)

@app.route('/character/pool')
@character_required
def character_pool():
    db = get_db()
    characters = db.fetchall('SELECT * FROM characters WHERE user_id = %s ORDER BY is_main DESC, created_at ASC',
                             (session['user_id'],))
    return render_template('character_pool.html', characters=characters)

@app.route('/character/<char_id>/set-main', methods=['POST'])
@login_required
def set_main_character(char_id):
    db = get_db()
    char = db.fetchone('SELECT * FROM characters WHERE id = %s AND user_id = %s', (char_id, session['user_id']))
    if not char:
        flash('Character not found.', 'error')
        return redirect(url_for('character_pool'))
    db.execute('UPDATE characters SET is_main = 0 WHERE user_id = %s', (session['user_id'],))
    db.execute('UPDATE characters SET is_main = 1 WHERE id = %s', (char_id,))
    db.execute('UPDATE users SET main_character_id = %s WHERE id = %s', (char_id, session['user_id']))
    flash('{} is now your main character!'.format(char['name']), 'success')
    return redirect(url_for('character_pool'))

@app.route('/character/<char_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_character(char_id):
    db = get_db()
    char = db.fetchone('SELECT * FROM characters WHERE id = %s AND user_id = %s', (char_id, session['user_id']))
    if not char:
        flash('Not found.', 'error')
        return redirect(url_for('character_pool'))
    if request.method == 'POST':
        n = request.form.get('char_name','').strip()
        race = request.form.get('char_race','')
        cls = request.form.get('char_class','')
        t1, t2, t3 = request.form.get('trait1',''), request.form.get('trait2',''), request.form.get('trait3','')
        bs = request.form.get('backstory','').strip()
        av = char['avatar_url']
        preset = request.form.get('preset_avatar', '')
        valid_presets = [a['file'] for a in PRESET_AVATARS]
        if preset and preset in valid_presets:
            av = preset
        elif 'avatar' in request.files and request.files['avatar'].filename:
            new_av = save_upload(request.files['avatar'], 'avatars')
            if new_av: av = new_av
        db.execute('UPDATE characters SET name=%s,race=%s,class=%s,trait1=%s,trait2=%s,trait3=%s,backstory=%s,avatar_url=%s WHERE id=%s',
                   (n, race, cls, t1, t2, t3, bs, av, char_id))
        flash('{} updated!'.format(n), 'success')
        return redirect(url_for('character_pool'))
    return render_template('edit_character.html', char=char, traits=CHARACTER_TRAITS,
                           preset_avatars=PRESET_AVATARS, races=CHARACTER_RACES,
                           race_labels=CHARACTER_RACE_LABELS, classes=CHARACTER_CLASSES)

@app.route('/character/<char_id>/delete', methods=['POST'])
@login_required
def delete_character(char_id):
    db = get_db()
    char = db.fetchone('SELECT * FROM characters WHERE id = %s AND user_id = %s', (char_id, session['user_id']))
    if not char: return redirect(url_for('character_pool'))
    cnt = db.fetchone('SELECT COUNT(*) as c FROM characters WHERE user_id = %s', (session['user_id'],))
    if cnt['c'] <= 1:
        flash('Cannot delete your only character!', 'error')
        return redirect(url_for('character_pool'))
    was_main = char['is_main']
    db.execute('DELETE FROM characters WHERE id = %s', (char_id,))
    if was_main:
        nxt = db.fetchone('SELECT id,name FROM characters WHERE user_id = %s ORDER BY created_at LIMIT 1', (session['user_id'],))
        if nxt:
            db.execute('UPDATE characters SET is_main = 1 WHERE id = %s', (nxt['id'],))
            db.execute('UPDATE users SET main_character_id = %s WHERE id = %s', (nxt['id'], session['user_id']))
    flash('{} removed.'.format(char['name']), 'info')
    return redirect(url_for('character_pool'))

# ─── Routes: Feed & Search ───────────────────────────────────────────────────

def _batch_fetch_sessions(db, posts):
    """Batch-fetch campaign sessions for a list of posts (fixes N+1 query)."""
    post_sessions = {}
    campaign_ids = [p['id'] for p in posts if p['post_type'] == 'campaign']
    if campaign_ids:
        placeholders = ','.join(['%s'] * len(campaign_ids))
        all_sessions = db.fetchall(
            'SELECT * FROM campaign_sessions WHERE post_id IN ({}) ORDER BY session_number ASC'.format(placeholders),
            tuple(campaign_ids))
        for s in all_sessions:
            post_sessions.setdefault(s['post_id'], []).append(s)
    return post_sessions

@app.route('/feed')
@character_required
def feed():
    db = get_db()
    uid = session['user_id']
    q = request.args.get('q', '').strip()
    try:
        page = max(1, int(request.args.get('page', 1)))
    except (ValueError, TypeError):
        page = 1
    per_page = 20
    offset = (page - 1) * per_page
    if q:
        like_q = '%{}%'.format(q)
        posts = db.fetchall('''
            SELECT p.*, u.username, c.name as char_name, c.avatar_url as char_avatar,
                   (SELECT COUNT(*) FROM likes WHERE post_id = p.id) as like_count,
                   (SELECT COUNT(*) FROM comments WHERE post_id = p.id) as comment_count,
                   (SELECT COUNT(*) FROM likes WHERE post_id = p.id AND user_id = %s) as user_liked
            FROM posts p JOIN users u ON p.author_id = u.id
            LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
            WHERE p.title LIKE %s OR p.content LIKE %s OR p.description LIKE %s
                  OR p.tag_location LIKE %s OR p.tag_age LIKE %s OR p.tag_characters LIKE %s
                  OR c.name LIKE %s OR u.username LIKE %s
            ORDER BY p.created_at DESC LIMIT 50
        ''', (uid, like_q, like_q, like_q, like_q, like_q, like_q, like_q, like_q))
        users_found = db.fetchall('''
            SELECT u.*, c.name as char_name, c.avatar_url as char_avatar, c.trait1
            FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
            WHERE u.username LIKE %s OR c.name LIKE %s LIMIT 10
        ''', (like_q, like_q))
        total = len(posts)
    else:
        users_found = []
        total_row = db.fetchone(
            'SELECT COUNT(*) as c FROM posts WHERE author_id NOT IN (SELECT blocked_id FROM blocks WHERE blocker_id = %s)',
            (uid,))
        total = total_row['c'] if total_row else 0
        posts = db.fetchall('''
            SELECT p.*, u.username, c.name as char_name, c.avatar_url as char_avatar,
                   (SELECT COUNT(*) FROM likes WHERE post_id = p.id) as like_count,
                   (SELECT COUNT(*) FROM comments WHERE post_id = p.id) as comment_count,
                   (SELECT COUNT(*) FROM likes WHERE post_id = p.id AND user_id = %s) as user_liked
            FROM posts p JOIN users u ON p.author_id = u.id
            LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
            WHERE p.author_id NOT IN (SELECT blocked_id FROM blocks WHERE blocker_id = %s)
            ORDER BY p.created_at DESC LIMIT %s OFFSET %s
        ''', (uid, uid, per_page, offset))
    post_sessions = _batch_fetch_sessions(db, posts)
    return render_template('feed.html', posts=posts, post_sessions=post_sessions,
                           search_query=q, users_found=users_found,
                           page=page, total_pages=(total + per_page - 1) // per_page)

# ─── Routes: Post Creation ───────────────────────────────────────────────────

@app.route('/post/create', methods=['GET', 'POST'])
@character_required
@limiter.limit("30 per hour")
def create_post():
    db = get_db()
    uid = session['user_id']
    own_chars = db.fetchall('SELECT id, name FROM characters WHERE user_id = %s', (uid,))
    if request.method == 'POST':
        post_type = request.form.get('post_type', 'story')
        title = request.form.get('title', '').strip()
        tag_location = request.form.get('tag_location', '').strip()
        tag_age = request.form.get('tag_age', '').strip()
        tag_characters = request.form.get('tag_characters', '').strip()
        tagged_users = request.form.get('tagged_users', '').strip()
        if not title:
            flash('A title is required!', 'error')
            return redirect(url_for('create_post'))
        post_id = str(uuid.uuid4())
        content = ''
        description = ''
        image_url = ''
        if post_type == 'story':
            content = request.form.get('content', '').strip()
            if not content:
                flash('Story content is required!', 'error')
                return redirect(url_for('create_post'))
        elif post_type == 'campaign':
            sessions_json = request.form.get('sessions_data', '[]')
            try:
                sessions = json.loads(sessions_json)
            except:
                sessions = []
            if not sessions:
                flash('Add at least one session!', 'error')
                return redirect(url_for('create_post'))
        elif post_type == 'art':
            description = request.form.get('description', '').strip()
            if 'image' in request.files:
                image_url = save_upload(request.files['image'], 'posts')
            if not image_url:
                flash('An image is required for art/map posts!', 'error')
                return redirect(url_for('create_post'))
        db.execute('''
            INSERT INTO posts (id, author_id, post_type, title, description, content, image_url,
                               tag_location, tag_age, tag_characters, tagged_users)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''', (post_id, uid, post_type, title, description, content, image_url,
              tag_location, tag_age, tag_characters, tagged_users))
        if post_type == 'campaign':
            for i, s in enumerate(sessions):
                sid = str(uuid.uuid4())
                db.execute('INSERT INTO campaign_sessions (id, post_id, session_number, title, content) VALUES (%s,%s,%s,%s,%s)',
                           (sid, post_id, i+1, s.get('title',''), s.get('content','')))
        flash('Your post has been shared with the realm!', 'success')
        return redirect(url_for('feed'))
    return render_template('create_post.html', own_chars=own_chars)

@app.route('/api/user-characters/<username>')
@login_required
def api_user_characters(username):
    db = get_db()
    user = db.fetchone('SELECT id FROM users WHERE username = %s', (username,))
    if not user: return jsonify([])
    chars = db.fetchall('SELECT id, name FROM characters WHERE user_id = %s', (user['id'],))
    return jsonify([{'id': c['id'], 'name': c['name']} for c in chars])

@app.route('/api/search-users')
@login_required
def api_search_users():
    q = request.args.get('q', '').strip()
    if len(q) < 2: return jsonify([])
    db = get_db()
    users = db.fetchall('''
        SELECT u.username, c.name as char_name
        FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE u.username LIKE %s AND u.id != %s LIMIT 8
    ''', ('%{}%'.format(q), session['user_id']))
    return jsonify([{'username': u['username'], 'char_name': u['char_name'] or u['username']} for u in users])

# ─── Routes: Post Interactions ────────────────────────────────────────────────

@app.route('/post/<post_id>/like', methods=['POST'])
@login_required
@limiter.limit("60 per minute")
def like_post(post_id):
    db = get_db()
    uid = session['user_id']
    # Verify post exists
    post = db.fetchone('SELECT id FROM posts WHERE id = %s', (post_id,))
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    try:
        existing = db.fetchone('SELECT user_id FROM likes WHERE user_id=%s AND post_id=%s', (uid, post_id))
        if existing:
            db.execute('DELETE FROM likes WHERE user_id=%s AND post_id=%s', (uid, post_id))
        else:
            db.execute('INSERT INTO likes (user_id, post_id) VALUES (%s,%s)', (uid, post_id))
    except Exception:
        # Handle race condition (duplicate key, etc.)
        pass
    cnt = db.fetchone('SELECT COUNT(*) as c FROM likes WHERE post_id=%s', (post_id,))
    return jsonify({'liked': not existing, 'count': cnt['c'] if cnt else 0})

@app.route('/post/<post_id>/comment', methods=['POST'])
@login_required
@limiter.limit("30 per minute")
def add_comment(post_id):
    content = request.form.get('content', '').strip()
    if not content: return jsonify({'error': 'Empty'}), 400
    if len(content) > 5000: return jsonify({'error': 'Comment too long (max 5000 characters)'}), 400
    db = get_db()
    # Verify post exists
    post = db.fetchone('SELECT id FROM posts WHERE id = %s', (post_id,))
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    try:
        cid = str(uuid.uuid4())
        db.execute('INSERT INTO comments (id, post_id, author_id, content) VALUES (%s,%s,%s,%s)',
                   (cid, post_id, session['user_id'], content))
    except Exception:
        return jsonify({'error': 'Failed to save comment'}), 500
    user = get_current_user()
    return jsonify({
        'id': cid, 'content': content,
        'author': user['char_name'] or user['username'],
        'username': user['username'],
        'avatar_url': user['char_avatar'] or '',
        'created_at': datetime.now().strftime('%b %d, %Y')
    })

@app.route('/post/<post_id>/comments')
@login_required
def get_comments(post_id):
    db = get_db()
    comments = db.fetchall('''
        SELECT cm.*, u.username, c.name as char_name, c.avatar_url as char_avatar
        FROM comments cm JOIN users u ON cm.author_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE cm.post_id = %s ORDER BY cm.created_at ASC
    ''', (post_id,))
    return jsonify([{
        'id': cm['id'], 'content': cm['content'],
        'author': cm['char_name'] or cm['username'],
        'username': cm['username'],
        'avatar_url': cm['char_avatar'] or '',
        'created_at': str(cm['created_at'])
    } for cm in comments])

@app.route('/post/<post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    db = get_db()
    post = db.fetchone('SELECT * FROM posts WHERE id=%s AND author_id=%s', (post_id, session['user_id']))
    if not post:
        flash('Post not found.', 'error')
        return redirect(url_for('feed'))
    db.execute('DELETE FROM campaign_sessions WHERE post_id=%s', (post_id,))
    db.execute('DELETE FROM comments WHERE post_id=%s', (post_id,))
    db.execute('DELETE FROM likes WHERE post_id=%s', (post_id,))
    db.execute('DELETE FROM posts WHERE id=%s', (post_id,))
    flash('Post deleted.', 'info')
    return redirect(url_for('feed'))

@app.route('/post/<post_id>')
@character_required
def post_detail(post_id):
    db = get_db()
    uid = session['user_id']
    post = db.fetchone('''
        SELECT p.*, u.username, c.name as char_name, c.avatar_url as char_avatar,
               (SELECT COUNT(*) FROM likes WHERE post_id = p.id) as like_count,
               (SELECT COUNT(*) FROM comments WHERE post_id = p.id) as comment_count,
               (SELECT COUNT(*) FROM likes WHERE post_id = p.id AND user_id = %s) as user_liked
        FROM posts p JOIN users u ON p.author_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE p.id = %s
    ''', (uid, post_id))
    if not post:
        flash('Post not found.', 'error')
        return redirect(url_for('feed'))
    sessions_data = []
    if post['post_type'] == 'campaign':
        sessions_data = db.fetchall('SELECT * FROM campaign_sessions WHERE post_id = %s ORDER BY session_number ASC', (post_id,))
    comments = db.fetchall('''
        SELECT cm.*, u.username, c.name as char_name, c.avatar_url as char_avatar
        FROM comments cm JOIN users u ON cm.author_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE cm.post_id = %s ORDER BY cm.created_at ASC
    ''', (post_id,))
    return render_template('post_detail.html', post=post,
                           sessions=sessions_data, comments=comments,
                           show_delete=(post['author_id'] == uid))

@app.route('/post/<post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    db = get_db()
    uid = session['user_id']
    post = db.fetchone('SELECT * FROM posts WHERE id = %s AND author_id = %s', (post_id, uid))
    if not post:
        flash('Post not found.', 'error')
        return redirect(url_for('feed'))
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash('Title is required.', 'error')
            return redirect(url_for('edit_post', post_id=post_id))
        if post['post_type'] == 'story':
            content = request.form.get('content', '').strip()
            db.execute('UPDATE posts SET title = %s, content = %s WHERE id = %s', (title, content, post_id))
        elif post['post_type'] == 'art':
            description = request.form.get('description', '').strip()
            image_url = post['image_url']
            if 'image' in request.files and request.files['image'].filename:
                new_url = save_upload(request.files['image'], 'posts')
                if new_url:
                    image_url = new_url
            db.execute('UPDATE posts SET title = %s, description = %s, image_url = %s WHERE id = %s',
                       (title, description, image_url, post_id))
        elif post['post_type'] == 'campaign':
            db.execute('UPDATE posts SET title = %s WHERE id = %s', (title, post_id))
        flash('Post updated!', 'success')
        return redirect(url_for('post_detail', post_id=post_id))
    return render_template('edit_post.html', post=post)

@app.route('/comment/<comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    db = get_db()
    uid = session['user_id']
    comment = db.fetchone('SELECT * FROM comments WHERE id = %s', (comment_id,))
    if not comment:
        return jsonify({'error': 'Not found'}), 404
    # Allow comment author or post author to delete
    post = db.fetchone('SELECT author_id FROM posts WHERE id = %s', (comment['post_id'],))
    if comment['author_id'] != uid and (not post or post['author_id'] != uid):
        return jsonify({'error': 'Unauthorized'}), 403
    db.execute('DELETE FROM comments WHERE id = %s', (comment_id,))
    return jsonify({'deleted': True})

# ─── Routes: Profile ─────────────────────────────────────────────────────────

@app.route('/profile/<username>')
@character_required
def profile(username):
    db = get_db()
    user = db.fetchone('''
        SELECT u.id, u.username, u.joined_at,
               c.id as char_id, c.name as char_name, c.race as char_race, c.class as char_class,
               c.trait1, c.trait2, c.trait3,
               c.backstory, c.avatar_url as char_avatar
        FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE u.username = %s
    ''', (username,))
    if not user:
        flash('User not found!', 'error')
        return redirect(url_for('feed'))
    try:
        page = max(1, int(request.args.get('page', 1)))
    except (ValueError, TypeError):
        page = 1
    per_page = 20
    offset = (page - 1) * per_page
    total_row = db.fetchone('SELECT COUNT(*) as c FROM posts WHERE author_id = %s', (user['id'],))
    total = total_row['c'] if total_row else 0
    posts = db.fetchall('''
        SELECT p.*, u.username, c.name as char_name, c.avatar_url as char_avatar,
               (SELECT COUNT(*) FROM likes WHERE post_id = p.id) as like_count,
               (SELECT COUNT(*) FROM comments WHERE post_id = p.id) as comment_count,
               (SELECT COUNT(*) FROM likes WHERE post_id = p.id AND user_id = %s) as user_liked
        FROM posts p JOIN users u ON p.author_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE p.author_id = %s ORDER BY p.created_at DESC LIMIT %s OFFSET %s
    ''', (session['user_id'], user['id'], per_page, offset))
    post_sessions = _batch_fetch_sessions(db, posts)
    all_characters = db.fetchall('SELECT * FROM characters WHERE user_id = %s ORDER BY is_main DESC, created_at', (user['id'],))
    fc = db.fetchone('SELECT COUNT(*) as c FROM follows WHERE followed_id=%s', (user['id'],))
    fing = db.fetchone('SELECT COUNT(*) as c FROM follows WHERE follower_id=%s', (user['id'],))
    is_following = False
    if session.get('user_id') != user['id']:
        is_following = db.fetchone('SELECT follower_id FROM follows WHERE follower_id=%s AND followed_id=%s',
                                   (session['user_id'], user['id'])) is not None
    return render_template('profile.html', profile_user=user, posts=posts, post_sessions=post_sessions,
                           all_characters=all_characters, follower_count=fc['c'], following_count=fing['c'],
                           is_following=is_following, page=page,
                           total_pages=(total + per_page - 1) // per_page, total_posts=total)

@app.route('/follow/<username>', methods=['POST'])
@login_required
def toggle_follow(username):
    db = get_db()
    target = db.fetchone('SELECT id FROM users WHERE username=%s', (username,))
    if not target or target['id'] == session['user_id']:
        return jsonify({'error': 'Invalid'}), 400
    try:
        existing = db.fetchone('SELECT follower_id FROM follows WHERE follower_id=%s AND followed_id=%s',
                               (session['user_id'], target['id']))
        if existing:
            db.execute('DELETE FROM follows WHERE follower_id=%s AND followed_id=%s', (session['user_id'], target['id']))
        else:
            db.execute('INSERT INTO follows (follower_id, followed_id) VALUES (%s,%s)', (session['user_id'], target['id']))
    except Exception:
        pass
    cnt = db.fetchone('SELECT COUNT(*) as c FROM follows WHERE followed_id=%s', (target['id'],))
    return jsonify({'following': not existing, 'follower_count': cnt['c'] if cnt else 0})

# ─── Report & Block System ──────────────────────────────────────────────────

@app.route('/report', methods=['POST'])
@login_required
@limiter.limit("10 per hour")
def submit_report():
    """Submit a report for a post, comment, or user."""
    reported_type = request.form.get('type', '').strip()  # 'post', 'comment', 'user', 'message'
    reported_id = request.form.get('id', '').strip()
    reason = request.form.get('reason', '').strip()
    if reported_type not in ('post', 'comment', 'user', 'message'):
        flash('Invalid report type.', 'error')
        return redirect(request.referrer or url_for('feed'))
    if not reported_id or not reason:
        flash('Please provide a reason for your report.', 'error')
        return redirect(request.referrer or url_for('feed'))
    if len(reason) > 1000:
        reason = reason[:1000]
    db = get_db()
    # Prevent duplicate reports
    existing = db.fetchone(
        'SELECT id FROM reports WHERE reporter_id = %s AND reported_type = %s AND reported_id = %s',
        (session['user_id'], reported_type, reported_id))
    if existing:
        flash('You have already reported this content.', 'info')
        return redirect(request.referrer or url_for('feed'))
    report_id = str(uuid.uuid4())
    db.execute(
        'INSERT INTO reports (id, reporter_id, reported_type, reported_id, reason) VALUES (%s,%s,%s,%s,%s)',
        (report_id, session['user_id'], reported_type, reported_id, reason))
    flash('Thank you — your report has been submitted and will be reviewed.', 'success')
    return redirect(request.referrer or url_for('feed'))

@app.route('/block/<username>', methods=['POST'])
@login_required
def toggle_block(username):
    """Block or unblock a user."""
    db = get_db()
    target = db.fetchone('SELECT id FROM users WHERE username = %s', (username,))
    if not target or target['id'] == session['user_id']:
        flash('Invalid action.', 'error')
        return redirect(request.referrer or url_for('feed'))
    existing = db.fetchone(
        'SELECT blocker_id FROM blocks WHERE blocker_id = %s AND blocked_id = %s',
        (session['user_id'], target['id']))
    if existing:
        db.execute('DELETE FROM blocks WHERE blocker_id = %s AND blocked_id = %s',
                   (session['user_id'], target['id']))
        # Also unfollow in both directions
        db.execute('DELETE FROM follows WHERE follower_id = %s AND followed_id = %s',
                   (session['user_id'], target['id']))
        db.execute('DELETE FROM follows WHERE follower_id = %s AND followed_id = %s',
                   (target['id'], session['user_id']))
        flash(f'@{username} has been unblocked.', 'success')
    else:
        db.execute('INSERT INTO blocks (blocker_id, blocked_id) VALUES (%s, %s)',
                   (session['user_id'], target['id']))
        # Unfollow in both directions
        db.execute('DELETE FROM follows WHERE follower_id = %s AND followed_id = %s',
                   (session['user_id'], target['id']))
        db.execute('DELETE FROM follows WHERE follower_id = %s AND followed_id = %s',
                   (target['id'], session['user_id']))
        flash(f'@{username} has been blocked. You won\'t see their content.', 'success')
    return redirect(request.referrer or url_for('feed'))

@app.route('/profile/<username>/followers')
@character_required
def followers_list(username):
    db = get_db()
    user = db.fetchone('SELECT id, username FROM users WHERE username = %s', (username,))
    if not user:
        flash('User not found.', 'error')
        return redirect(url_for('feed'))
    followers = db.fetchall('''
        SELECT u.*, c.name as char_name, c.avatar_url as char_avatar, c.trait1
        FROM follows f JOIN users u ON f.follower_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE f.followed_id = %s ORDER BY f.created_at DESC
    ''', (user['id'],))
    return render_template('follow_list.html', profile_username=username,
                           users=followers, list_type='Followers')

@app.route('/profile/<username>/following')
@character_required
def following_list(username):
    db = get_db()
    user = db.fetchone('SELECT id, username FROM users WHERE username = %s', (username,))
    if not user:
        flash('User not found.', 'error')
        return redirect(url_for('feed'))
    following = db.fetchall('''
        SELECT u.*, c.name as char_name, c.avatar_url as char_avatar, c.trait1
        FROM follows f JOIN users u ON f.followed_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE f.follower_id = %s ORDER BY f.created_at DESC
    ''', (user['id'],))
    return render_template('follow_list.html', profile_username=username,
                           users=following, list_type='Following')

@app.route('/explore')
@character_required
def explore():
    db = get_db()
    uid = session['user_id']
    try:
        page = max(1, int(request.args.get('page', 1)))
    except (ValueError, TypeError):
        page = 1
    per_page = 20
    offset = (page - 1) * per_page
    total_row = db.fetchone('SELECT COUNT(*) as c FROM posts')
    total = total_row['c'] if total_row else 0
    posts = db.fetchall('''
        SELECT p.*, u.username, c.name as char_name, c.avatar_url as char_avatar,
               (SELECT COUNT(*) FROM likes WHERE post_id = p.id) as like_count,
               (SELECT COUNT(*) FROM comments WHERE post_id = p.id) as comment_count,
               (SELECT COUNT(*) FROM likes WHERE post_id = p.id AND user_id = %s) as user_liked
        FROM posts p JOIN users u ON p.author_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        ORDER BY like_count DESC, p.created_at DESC LIMIT %s OFFSET %s
    ''', (uid, per_page, offset))
    post_sessions = _batch_fetch_sessions(db, posts)
    suggested = db.fetchall('''
        SELECT u.*, c.name as char_name, c.avatar_url as char_avatar, c.trait1,
               (SELECT COUNT(*) FROM follows WHERE followed_id = u.id) as follower_count
        FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE u.id != %s AND u.id NOT IN (SELECT followed_id FROM follows WHERE follower_id = %s)
        ORDER BY follower_count DESC LIMIT 10
    ''', (uid, uid))
    return render_template('explore.html', posts=posts, post_sessions=post_sessions,
                           suggested_users=suggested,
                           page=page, total_pages=(total + per_page - 1) // per_page)

# ─── Routes: Direct Messages ─────────────────────────────────────────────────

def get_or_create_conversation(user1_id, user2_id):
    db = get_db()
    conv = db.fetchone('''
        SELECT * FROM conversations
        WHERE (user1_id = %s AND user2_id = %s) OR (user1_id = %s AND user2_id = %s)
    ''', (user1_id, user2_id, user2_id, user1_id))
    if conv: return conv['id']
    conv_id = str(uuid.uuid4())
    db.execute('INSERT INTO conversations (id, user1_id, user2_id) VALUES (%s,%s,%s)', (conv_id, user1_id, user2_id))
    return conv_id

@app.route('/messages')
@character_required
def messages_inbox():
    db = get_db()
    uid = session['user_id']
    conversations = db.fetchall('''
        SELECT cv.*,
            CASE WHEN cv.user1_id = %s THEN cv.user2_id ELSE cv.user1_id END as other_id,
            (SELECT content FROM messages WHERE conversation_id = cv.id ORDER BY created_at DESC LIMIT 1) as last_message,
            (SELECT created_at FROM messages WHERE conversation_id = cv.id ORDER BY created_at DESC LIMIT 1) as last_msg_time,
            (SELECT COUNT(*) FROM messages WHERE conversation_id = cv.id AND sender_id != %s AND is_read = 0) as unread
        FROM conversations cv
        WHERE cv.user1_id = %s OR cv.user2_id = %s
        ORDER BY last_message_at DESC
    ''', (uid, uid, uid, uid))
    conv_data = []
    for cv in conversations:
        other = db.fetchone('''
            SELECT u.*, c.name as char_name, c.avatar_url as char_avatar
            FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
            WHERE u.id = %s
        ''', (cv['other_id'],))
        if other:
            conv_data.append({'conv': cv, 'other': other})
    return render_template('messages_inbox.html', conversations=conv_data)

@app.route('/messages/<username>', methods=['GET', 'POST'])
@character_required
def messages_conversation(username):
    db = get_db()
    uid = session['user_id']
    other = db.fetchone('''
        SELECT u.*, c.name as char_name, c.avatar_url as char_avatar
        FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE u.username = %s
    ''', (username,))
    if not other or other['id'] == uid:
        flash('Cannot message this user.', 'error')
        return redirect(url_for('messages_inbox'))
    conv_id = get_or_create_conversation(uid, other['id'])
    if request.method == 'POST':
        content = request.form.get('content', '').strip()
        if content and len(content) <= 5000:
            msg_id = str(uuid.uuid4())
            db.execute('INSERT INTO messages (id, conversation_id, sender_id, content) VALUES (%s,%s,%s,%s)',
                       (msg_id, conv_id, uid, content))
            db.execute('UPDATE conversations SET last_message_at = CURRENT_TIMESTAMP WHERE id = %s', (conv_id,))
        return redirect(url_for('messages_conversation', username=username))
    db.execute('UPDATE messages SET is_read = 1 WHERE conversation_id = %s AND sender_id != %s AND is_read = 0', (conv_id, uid))
    msgs = db.fetchall('''
        SELECT m.*, u.username as sender_username,
               c.name as sender_char_name, c.avatar_url as sender_avatar
        FROM messages m JOIN users u ON m.sender_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE m.conversation_id = %s ORDER BY m.created_at ASC
    ''', (conv_id,))
    return render_template('messages_conversation.html', other=other, messages=msgs, conv_id=conv_id)

@app.route('/messages/<username>/send', methods=['POST'])
@login_required
@limiter.limit("60 per minute")
def send_message_api(username):
    db = get_db()
    uid = session['user_id']
    other = db.fetchone('SELECT id FROM users WHERE username = %s', (username,))
    if not other or other['id'] == uid: return jsonify({'error': 'Invalid'}), 400
    # Check for blocks in either direction
    blocked = db.fetchone(
        'SELECT blocker_id FROM blocks WHERE (blocker_id=%s AND blocked_id=%s) OR (blocker_id=%s AND blocked_id=%s)',
        (uid, other['id'], other['id'], uid))
    if blocked: return jsonify({'error': 'Cannot send message to this user.'}), 403
    content = request.form.get('content', '').strip()
    if not content: return jsonify({'error': 'Empty'}), 400
    if len(content) > 5000: return jsonify({'error': 'Message too long (max 5000 characters)'}), 400
    conv_id = get_or_create_conversation(uid, other['id'])
    msg_id = str(uuid.uuid4())
    db.execute('INSERT INTO messages (id, conversation_id, sender_id, content) VALUES (%s,%s,%s,%s)',
               (msg_id, conv_id, uid, content))
    db.execute('UPDATE conversations SET last_message_at = CURRENT_TIMESTAMP WHERE id = %s', (conv_id,))
    user = get_current_user()
    return jsonify({
        'id': msg_id, 'content': content,
        'sender_char_name': user['char_name'] or user['username'],
        'sender_avatar': user['char_avatar'] or '',
        'sender_username': user['username'],
        'created_at': datetime.now().strftime('%b %d, %Y %I:%M %p'),
        'is_mine': True
    })

@app.route('/messages/<username>/poll')
@login_required
def poll_messages(username):
    db = get_db()
    uid = session['user_id']
    other = db.fetchone('SELECT id FROM users WHERE username = %s', (username,))
    if not other: return jsonify([])
    after = request.args.get('after', '')
    conv = db.fetchone('''
        SELECT id FROM conversations
        WHERE (user1_id = %s AND user2_id = %s) OR (user1_id = %s AND user2_id = %s)
    ''', (uid, other['id'], other['id'], uid))
    if not conv: return jsonify([])
    msgs = db.fetchall('''
        SELECT m.*, u.username as sender_username,
               c.name as sender_char_name, c.avatar_url as sender_avatar
        FROM messages m JOIN users u ON m.sender_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE m.conversation_id = %s AND m.created_at > %s
        ORDER BY m.created_at ASC
    ''', (conv['id'], after))
    db.execute('UPDATE messages SET is_read = 1 WHERE conversation_id = %s AND sender_id != %s AND is_read = 0',
               (conv['id'], uid))
    return jsonify([{
        'id': m['id'], 'content': m['content'],
        'sender_char_name': m['sender_char_name'] or m['sender_username'],
        'sender_avatar': m['sender_avatar'] or '',
        'sender_username': m['sender_username'],
        'created_at': str(m['created_at']),
        'is_mine': m['sender_id'] == uid
    } for m in msgs])

# ─── Routes: The Annals of Elysal ────────────────────────────────────────────

@app.route('/annals')
@character_required
def annals_home():
    return render_template('annals_home.html', intro=ANNALS_INTRO, ages=ANNALS_AGES)

@app.route('/annals/age/<int:age_num>')
@character_required
def annals_age(age_num):
    age = next((a for a in ANNALS_AGES if a['number'] == age_num), None)
    if not age:
        flash('Age not found.', 'error')
        return redirect(url_for('annals_home'))
    return render_template('annals_age.html', age=age, ages=ANNALS_AGES)

@app.route('/annals/age/<int:age_num>/century/<int:century_num>')
@character_required
def annals_century(age_num, century_num):
    age = next((a for a in ANNALS_AGES if a['number'] == age_num), None)
    if not age:
        flash('Age not found.', 'error')
        return redirect(url_for('annals_home'))
    century = next((c for c in age['centuries'] if c['number'] == century_num), None)
    if not century:
        flash('Century not found.', 'error')
        return redirect(url_for('annals_age', age_num=age_num))
    # Fetch user-contributed stories for this century
    db = get_db()
    user_stories = db.fetchall('''
        SELECT a.*, u.username, c.name as char_name, c.avatar_url as char_avatar
        FROM annals_stories a JOIN users u ON a.author_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE a.age_number = %s AND a.century_number = %s
        ORDER BY a.created_at DESC
    ''', (age_num, century_num))
    return render_template('annals_century.html', age=age, century=century, ages=ANNALS_AGES, user_stories=user_stories)

@app.route('/annals/age/<int:age_num>/century/<int:century_num>/story/<int:story_idx>')
@character_required
def annals_story(age_num, century_num, story_idx):
    age = next((a for a in ANNALS_AGES if a['number'] == age_num), None)
    if not age: return redirect(url_for('annals_home'))
    century = next((c for c in age['centuries'] if c['number'] == century_num), None)
    if not century or story_idx < 0 or story_idx >= len(century['stories']):
        return redirect(url_for('annals_century', age_num=age_num, century_num=century_num))
    story = century['stories'][story_idx]
    return render_template('annals_story.html', age=age, century=century, story=story,
                           story_idx=story_idx, ages=ANNALS_AGES)

@app.route('/annals/search')
@character_required
def annals_search():
    q = request.args.get('q', '').strip().lower()
    results = []
    if q and len(q) >= 2:
        for age in ANNALS_AGES:
            if q in age['name'].lower() or q in age['description'].lower():
                results.append({'type': 'age', 'age': age, 'title': age['name'], 'snippet': age['description'][:200]})
            for century in age['centuries']:
                if q in century['name'].lower() or q in century['description'].lower():
                    results.append({'type': 'century', 'age': age, 'century': century,
                                    'title': '{} - {}'.format(century['name'], age['name']), 'snippet': century['description'][:200]})
                for si, story in enumerate(century['stories']):
                    if q in story['title'].lower() or q in story['content'].lower():
                        idx = story['content'].lower().find(q)
                        start = max(0, idx - 60)
                        end = min(len(story['content']), idx + 60)
                        snippet = ('...' if start > 0 else '') + story['content'][start:end] + ('...' if end < len(story['content']) else '')
                        results.append({'type': 'story', 'age': age, 'century': century,
                                        'story_idx': si, 'title': story['title'], 'snippet': snippet})
        # Also search user-contributed stories
        db = get_db()
        user_stories = db.fetchall('''
            SELECT a.*, u.username FROM annals_stories a
            JOIN users u ON a.author_id = u.id
            WHERE LOWER(a.title) LIKE %s OR LOWER(a.content) LIKE %s
            ORDER BY a.created_at DESC LIMIT 50
        ''', (f'%{q}%', f'%{q}%'))
        for us in user_stories:
            age = next((a for a in ANNALS_AGES if a['number'] == us['age_number']), None)
            if age:
                century = next((c for c in age['centuries'] if c['number'] == us['century_number']), None)
                if century:
                    idx = us['content'].lower().find(q)
                    start = max(0, idx - 60)
                    end = min(len(us['content']), idx + 60)
                    snippet = ('...' if start > 0 else '') + us['content'][start:end] + ('...' if end < len(us['content']) else '')
                    results.append({'type': 'user_story', 'age': age, 'century': century,
                                    'story_id': us['id'], 'title': us['title'],
                                    'snippet': snippet, 'username': us['username']})
    return render_template('annals_search.html', q=request.args.get('q', ''), results=results, ages=ANNALS_AGES)

@app.route('/annals/contribute', methods=['GET', 'POST'])
@character_required
def annals_contribute():
    if request.method == 'POST':
        try:
            age_num = int(request.form.get('age_number', 0))
        except (ValueError, TypeError):
            age_num = 0
        try:
            century_num = int(request.form.get('century_number', 0))
        except (ValueError, TypeError):
            century_num = 0
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        errors = []
        age = next((a for a in ANNALS_AGES if a['number'] == age_num), None)
        if not age:
            errors.append('Select a valid age.')
        else:
            century = next((c for c in age['centuries'] if c['number'] == century_num), None)
            if not century:
                errors.append('Select a valid century.')
        if len(title) < 3:
            errors.append('Title must be at least 3 characters.')
        if len(content) < 50:
            errors.append('Story must be at least 50 characters.')
        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('annals_contribute.html', ages=ANNALS_AGES,
                                   sel_age=age_num, sel_century=century_num, title=title, content=content)
        db = get_db()
        story_id = str(uuid.uuid4())
        db.execute('INSERT INTO annals_stories (id, author_id, age_number, century_number, title, content) VALUES (%s,%s,%s,%s,%s,%s)',
                   (story_id, session['user_id'], age_num, century_num, title, content))
        flash('Your story has been added to the Annals!', 'success')
        return redirect(url_for('annals_century', age_num=age_num, century_num=century_num))
    # Pre-select age/century if passed via query params
    sel_age = request.args.get('age', 0, type=int)
    sel_century = request.args.get('century', 0, type=int)
    return render_template('annals_contribute.html', ages=ANNALS_AGES,
                           sel_age=sel_age, sel_century=sel_century, title='', content='')

@app.route('/annals/story/<story_id>')
@character_required
def annals_user_story(story_id):
    db = get_db()
    story = db.fetchone('''
        SELECT a.*, u.username, c.name as char_name, c.avatar_url as char_avatar
        FROM annals_stories a JOIN users u ON a.author_id = u.id
        LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE a.id = %s
    ''', (story_id,))
    if not story:
        flash('Story not found.', 'error')
        return redirect(url_for('annals_home'))
    age = next((a for a in ANNALS_AGES if a['number'] == story['age_number']), None)
    century = next((c for c in age['centuries'] if c['number'] == story['century_number']), None) if age else None
    return render_template('annals_user_story.html', story=story, age=age, century=century, ages=ANNALS_AGES)

@app.route('/annals/story/<story_id>/edit', methods=['GET', 'POST'])
@login_required
def annals_edit_story(story_id):
    db = get_db()
    story = db.fetchone('SELECT * FROM annals_stories WHERE id = %s AND author_id = %s', (story_id, session['user_id']))
    if not story:
        flash('Story not found or not yours.', 'error')
        return redirect(url_for('annals_home'))
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        if len(title) < 3:
            flash('Title must be 3+ characters.', 'error')
        elif len(content) < 50:
            flash('Story must be 50+ characters.', 'error')
        else:
            db.execute('UPDATE annals_stories SET title = %s, content = %s WHERE id = %s',
                       (title, content, story_id))
            flash('Story updated!', 'success')
            return redirect(url_for('annals_user_story', story_id=story_id))
    age = next((a for a in ANNALS_AGES if a['number'] == story['age_number']), None)
    century = next((c for c in age['centuries'] if c['number'] == story['century_number']), None) if age else None
    return render_template('annals_edit_story.html', story=story, age=age, century=century, ages=ANNALS_AGES)

@app.route('/annals/story/<story_id>/delete', methods=['POST'])
@login_required
def annals_delete_story(story_id):
    db = get_db()
    story = db.fetchone('SELECT * FROM annals_stories WHERE id = %s AND author_id = %s', (story_id, session['user_id']))
    if not story:
        flash('Story not found or not yours.', 'error')
        return redirect(url_for('annals_home'))
    db.execute('DELETE FROM annals_stories WHERE id = %s', (story_id,))
    flash('Story removed from the Annals.', 'info')
    return redirect(url_for('annals_century', age_num=story['age_number'], century_num=story['century_number']))

# ─── Init ─────────────────────────────────────────────────────────────────────

print("\n🧌 Poetic Goblin — Starting up...")
print(Config.summary())
print()

with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=not Config.is_production(), port=5000)
