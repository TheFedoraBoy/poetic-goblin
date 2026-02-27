"""Poetic Goblin — Auth Blueprint (register, login, logout, verify, password reset)"""

import re
import uuid
import secrets
from datetime import datetime, timedelta

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from database import get_db
from email_service import send_verification_email, send_password_reset_email
from extensions import limiter
from helpers import login_required, validate_password

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
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
            return redirect(url_for('auth.login'))
        else:
            session['user_id'] = user_id
            session.permanent = True
            flash('Account created! Now forge your first character.', 'success')
            return redirect(url_for('characters.create_character'))
    return render_template('register.html')


@bp.route('/verify/<token>')
def verify_email(token):
    db = get_db()
    user = db.fetchone('SELECT id, username, joined_at FROM users WHERE verification_token = %s AND email_verified = 0', (token,))
    if not user:
        flash('Invalid or expired verification link.', 'error')
        return redirect(url_for('auth.login'))
    try:
        joined = user['joined_at']
        if isinstance(joined, str):
            joined = datetime.strptime(joined, '%Y-%m-%d %H:%M:%S')
        if datetime.now() - joined > timedelta(hours=Config.VERIFICATION_TOKEN_HOURS):
            flash('Verification link has expired. Please register again.', 'error')
            return redirect(url_for('auth.register'))
    except (ValueError, TypeError):
        pass
    db.execute("UPDATE users SET email_verified = 1, verification_token = '' WHERE id = %s", (user['id'],))
    flash('Email verified! Welcome, {}. You may now log in.'.format(user['username']), 'success')
    return redirect(url_for('auth.login'))


@bp.route('/login', methods=['GET', 'POST'])
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
            session.permanent = True
            if not db.fetchone('SELECT id FROM characters WHERE user_id = %s', (user['id'],)):
                return redirect(url_for('characters.create_character'))
            flash('Welcome back!', 'success')
            return redirect(url_for('posts.feed'))
        flash('Invalid credentials.', 'error')
    return render_template('login.html')


@bp.route('/resend-verification', methods=['POST'])
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
    flash('If that account exists, a verification email has been sent.', 'success')
    return redirect(url_for('auth.login'))


@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    session.clear()
    flash('Logged out. Safe travels!', 'info')
    return redirect(url_for('index'))


@bp.route('/forgot-password', methods=['GET', 'POST'])
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
        return redirect(url_for('auth.login'))
    return render_template('forgot_password.html')


@bp.route('/reset-password/<token>', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
def reset_password(token):
    db = get_db()
    user = db.fetchone(
        'SELECT id, username FROM users WHERE reset_token = %s AND reset_token_expires > %s',
        (token, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    if not user:
        flash('Invalid or expired reset link.', 'error')
        return redirect(url_for('auth.forgot_password'))
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
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html', token=token)
