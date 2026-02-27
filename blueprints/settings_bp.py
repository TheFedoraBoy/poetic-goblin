"""Poetic Goblin — Settings Blueprint (account settings, delete account)"""

import secrets
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from database import get_db
from email_service import send_verification_email
from helpers import login_required, validate_password

bp = Blueprint('settings', __name__)


@bp.route('/settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    db = get_db()
    user = db.fetchone('SELECT id, username, email, password_hash, email_verified, show_explicit, joined_at FROM users WHERE id = %s', (session['user_id'],))
    if not user:
        session.clear()
        return redirect(url_for('auth.login'))
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
        elif action == 'toggle_explicit':
            new_val = 1 if request.form.get('show_explicit') == '1' else 0
            db.execute('UPDATE users SET show_explicit = %s WHERE id = %s', (new_val, user['id']))
            flash('Content preferences updated!', 'success')
        return redirect(url_for('settings.account_settings'))
    return render_template('settings.html', user=user)


@bp.route('/settings/delete-account', methods=['POST'])
@login_required
def delete_account():
    db = get_db()
    password = request.form.get('password', '')
    user = db.fetchone('SELECT id, password_hash FROM users WHERE id = %s', (session['user_id'],))
    if not user or not check_password_hash(user['password_hash'], password):
        flash('Incorrect password. Account not deleted.', 'error')
        return redirect(url_for('settings.account_settings'))
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
