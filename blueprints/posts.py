"""Poetic Goblin — Posts Blueprint (feed, create, edit, delete, like, comment, explore)"""

import uuid
import json
import logging
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify

from database import get_db
from storage import save_upload
from moderation import is_text_allowed, check_image_safety
from extensions import limiter
from helpers import (login_required, character_required, get_current_user,
                     escape_like, censor_filter)

logger = logging.getLogger('poetic_goblin')
bp = Blueprint('posts', __name__)


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


@bp.route('/feed')
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
        like_q = '%{}%'.format(escape_like(q))
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


@bp.route('/post/create', methods=['GET', 'POST'])
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
            return redirect(url_for('posts.create_post'))
        allowed, reason = is_text_allowed(title)
        if not allowed:
            flash(reason, 'error')
            return redirect(url_for('posts.create_post'))
        post_id = str(uuid.uuid4())
        content = ''
        description = ''
        image_url = ''
        if post_type == 'story':
            content = request.form.get('content', '').strip()
            if not content:
                flash('Story content is required!', 'error')
                return redirect(url_for('posts.create_post'))
            allowed, reason = is_text_allowed(content)
            if not allowed:
                flash(reason, 'error')
                return redirect(url_for('posts.create_post'))
        elif post_type == 'campaign':
            sessions_json = request.form.get('sessions_data', '[]')
            try:
                sessions = json.loads(sessions_json)
            except Exception:
                sessions = []
            if not sessions:
                flash('Add at least one session!', 'error')
                return redirect(url_for('posts.create_post'))
            for s in sessions:
                session_text = '{} {}'.format(s.get('title', ''), s.get('content', ''))
                allowed, reason = is_text_allowed(session_text)
                if not allowed:
                    flash(reason, 'error')
                    return redirect(url_for('posts.create_post'))
        elif post_type == 'art':
            description = request.form.get('description', '').strip()
            if description:
                allowed, reason = is_text_allowed(description)
                if not allowed:
                    flash(reason, 'error')
                    return redirect(url_for('posts.create_post'))
            if 'image' in request.files:
                img_file = request.files['image']
                if img_file and img_file.filename:
                    safe, img_reason = check_image_safety(img_file)
                    if not safe:
                        flash(img_reason, 'error')
                        return redirect(url_for('posts.create_post'))
                image_url = save_upload(img_file, 'posts')
            if not image_url:
                flash('An image is required for art/map posts!', 'error')
                return redirect(url_for('posts.create_post'))
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
        return redirect(url_for('posts.feed'))
    return render_template('create_post.html', own_chars=own_chars)


@bp.route('/api/user-characters/<username>')
@login_required
def api_user_characters(username):
    db = get_db()
    user = db.fetchone('SELECT id FROM users WHERE username = %s', (username,))
    if not user: return jsonify([])
    chars = db.fetchall('SELECT id, name FROM characters WHERE user_id = %s', (user['id'],))
    return jsonify([{'id': c['id'], 'name': c['name']} for c in chars])


@bp.route('/api/search-users')
@login_required
def api_search_users():
    q = request.args.get('q', '').strip()
    if len(q) < 2: return jsonify([])
    db = get_db()
    users = db.fetchall('''
        SELECT u.username, c.name as char_name
        FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
        WHERE u.username LIKE %s AND u.id != %s LIMIT 8
    ''', ('%{}%'.format(escape_like(q)), session['user_id']))
    return jsonify([{'username': u['username'], 'char_name': u['char_name'] or u['username']} for u in users])


@bp.route('/post/<post_id>/like', methods=['POST'])
@login_required
@limiter.limit("60 per minute")
def like_post(post_id):
    db = get_db()
    uid = session['user_id']
    post = db.fetchone('SELECT id FROM posts WHERE id = %s', (post_id,))
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    try:
        existing = db.fetchone('SELECT user_id FROM likes WHERE user_id=%s AND post_id=%s', (uid, post_id))
        if existing:
            db.execute('DELETE FROM likes WHERE user_id=%s AND post_id=%s', (uid, post_id))
        else:
            db.execute('INSERT INTO likes (user_id, post_id) VALUES (%s,%s)', (uid, post_id))
    except Exception as e:
        logger.debug('Like toggle race condition for post %s: %s', post_id, e)
    cnt = db.fetchone('SELECT COUNT(*) as c FROM likes WHERE post_id=%s', (post_id,))
    return jsonify({'liked': not existing, 'count': cnt['c'] if cnt else 0})


@bp.route('/post/<post_id>/comment', methods=['POST'])
@login_required
@limiter.limit("30 per minute")
def add_comment(post_id):
    content = request.form.get('content', '').strip()
    if not content: return jsonify({'error': 'Empty'}), 400
    if len(content) > 5000: return jsonify({'error': 'Comment too long (max 5000 characters)'}), 400
    allowed, reason = is_text_allowed(content)
    if not allowed:
        return jsonify({'error': reason}), 400
    db = get_db()
    post = db.fetchone('SELECT id FROM posts WHERE id = %s', (post_id,))
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    try:
        cid = str(uuid.uuid4())
        db.execute('INSERT INTO comments (id, post_id, author_id, content) VALUES (%s,%s,%s,%s)',
                   (cid, post_id, session['user_id'], content))
    except Exception as e:
        logger.error('Failed to save comment on post %s: %s', post_id, e)
        return jsonify({'error': 'Failed to save comment'}), 500
    user = get_current_user()
    return jsonify({
        'id': cid, 'content': censor_filter(content),
        'author': user['char_name'] or user['username'],
        'username': user['username'],
        'avatar_url': user['char_avatar'] or '',
        'created_at': datetime.now().strftime('%b %d, %Y')
    })


@bp.route('/post/<post_id>/comments')
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
        'id': cm['id'], 'content': censor_filter(cm['content']),
        'author': cm['char_name'] or cm['username'],
        'username': cm['username'],
        'avatar_url': cm['char_avatar'] or '',
        'created_at': str(cm['created_at'])
    } for cm in comments])


@bp.route('/post/<post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    db = get_db()
    post = db.fetchone('SELECT * FROM posts WHERE id=%s AND author_id=%s', (post_id, session['user_id']))
    if not post:
        flash('Post not found.', 'error')
        return redirect(url_for('posts.feed'))
    db.execute('DELETE FROM campaign_sessions WHERE post_id=%s', (post_id,))
    db.execute('DELETE FROM comments WHERE post_id=%s', (post_id,))
    db.execute('DELETE FROM likes WHERE post_id=%s', (post_id,))
    db.execute('DELETE FROM posts WHERE id=%s', (post_id,))
    flash('Post deleted.', 'info')
    return redirect(url_for('posts.feed'))


@bp.route('/post/<post_id>')
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
        return redirect(url_for('posts.feed'))
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


@bp.route('/post/<post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    db = get_db()
    uid = session['user_id']
    post = db.fetchone('SELECT * FROM posts WHERE id = %s AND author_id = %s', (post_id, uid))
    if not post:
        flash('Post not found.', 'error')
        return redirect(url_for('posts.feed'))
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash('Title is required.', 'error')
            return redirect(url_for('posts.edit_post', post_id=post_id))
        allowed, reason = is_text_allowed(title)
        if not allowed:
            flash(reason, 'error')
            return redirect(url_for('posts.edit_post', post_id=post_id))
        if post['post_type'] == 'story':
            content = request.form.get('content', '').strip()
            allowed, reason = is_text_allowed(content)
            if not allowed:
                flash(reason, 'error')
                return redirect(url_for('posts.edit_post', post_id=post_id))
            db.execute('UPDATE posts SET title = %s, content = %s WHERE id = %s', (title, content, post_id))
        elif post['post_type'] == 'art':
            description = request.form.get('description', '').strip()
            if description:
                allowed, reason = is_text_allowed(description)
                if not allowed:
                    flash(reason, 'error')
                    return redirect(url_for('posts.edit_post', post_id=post_id))
            image_url = post['image_url']
            if 'image' in request.files and request.files['image'].filename:
                img_file = request.files['image']
                safe, img_reason = check_image_safety(img_file)
                if not safe:
                    flash(img_reason, 'error')
                    return redirect(url_for('posts.edit_post', post_id=post_id))
                new_url = save_upload(img_file, 'posts')
                if new_url:
                    image_url = new_url
            db.execute('UPDATE posts SET title = %s, description = %s, image_url = %s WHERE id = %s',
                       (title, description, image_url, post_id))
        elif post['post_type'] == 'campaign':
            db.execute('UPDATE posts SET title = %s WHERE id = %s', (title, post_id))
        flash('Post updated!', 'success')
        return redirect(url_for('posts.post_detail', post_id=post_id))
    return render_template('edit_post.html', post=post)


@bp.route('/comment/<comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    db = get_db()
    uid = session['user_id']
    comment = db.fetchone('SELECT * FROM comments WHERE id = %s', (comment_id,))
    if not comment:
        return jsonify({'error': 'Not found'}), 404
    post = db.fetchone('SELECT author_id FROM posts WHERE id = %s', (comment['post_id'],))
    if comment['author_id'] != uid and (not post or post['author_id'] != uid):
        return jsonify({'error': 'Unauthorized'}), 403
    db.execute('DELETE FROM comments WHERE id = %s', (comment_id,))
    return jsonify({'deleted': True})


@bp.route('/explore')
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
