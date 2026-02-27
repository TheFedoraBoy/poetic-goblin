"""Poetic Goblin — Characters Blueprint"""

import uuid
from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from database import get_db
from storage import save_upload
from moderation import check_image_safety
from helpers import (login_required, character_required,
                     CHARACTER_TRAITS, PRESET_AVATARS, CHARACTER_RACES,
                     CHARACTER_RACE_LABELS, CHARACTER_CLASSES)

bp = Blueprint('characters', __name__)


@bp.route('/character/create', methods=['GET', 'POST'])
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
            img_file = request.files['avatar']
            safe, img_reason = check_image_safety(img_file)
            if not safe:
                flash(img_reason, 'error')
                return redirect(url_for('characters.create_character'))
            avatar_url = save_upload(img_file, 'avatars')
        existing = db.fetchone('SELECT COUNT(*) as c FROM characters WHERE user_id = %s', (session['user_id'],))
        is_main = 1 if (not existing or existing['c'] == 0) else 0
        char_id = str(uuid.uuid4())
        db.execute('INSERT INTO characters (id,user_id,name,race,class,trait1,trait2,trait3,backstory,avatar_url,is_main) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                   (char_id, session['user_id'], char_name, char_race, char_class, trait1, trait2, trait3, backstory, avatar_url, is_main))
        if is_main:
            db.execute('UPDATE users SET main_character_id = %s WHERE id = %s', (char_id, session['user_id']))
        flash('{} has entered the realm!'.format(char_name), 'success')
        return redirect(url_for('posts.feed'))
    return render_template('create_character.html', traits=CHARACTER_TRAITS,
                           char_name='', char_race='', char_class='',
                           trait1='', trait2='', trait3='', backstory='',
                           preset_avatars=PRESET_AVATARS, races=CHARACTER_RACES,
                           race_labels=CHARACTER_RACE_LABELS, classes=CHARACTER_CLASSES)


@bp.route('/character/pool')
@character_required
def character_pool():
    db = get_db()
    characters = db.fetchall('SELECT * FROM characters WHERE user_id = %s ORDER BY is_main DESC, created_at ASC',
                             (session['user_id'],))
    return render_template('character_pool.html', characters=characters)


@bp.route('/character/<char_id>/set-main', methods=['POST'])
@login_required
def set_main_character(char_id):
    db = get_db()
    char = db.fetchone('SELECT * FROM characters WHERE id = %s AND user_id = %s', (char_id, session['user_id']))
    if not char:
        flash('Character not found.', 'error')
        return redirect(url_for('characters.character_pool'))
    db.execute('UPDATE characters SET is_main = 0 WHERE user_id = %s', (session['user_id'],))
    db.execute('UPDATE characters SET is_main = 1 WHERE id = %s', (char_id,))
    db.execute('UPDATE users SET main_character_id = %s WHERE id = %s', (char_id, session['user_id']))
    flash('{} is now your main character!'.format(char['name']), 'success')
    return redirect(url_for('characters.character_pool'))


@bp.route('/character/<char_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_character(char_id):
    db = get_db()
    char = db.fetchone('SELECT * FROM characters WHERE id = %s AND user_id = %s', (char_id, session['user_id']))
    if not char:
        flash('Not found.', 'error')
        return redirect(url_for('characters.character_pool'))
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
            img_file = request.files['avatar']
            safe, img_reason = check_image_safety(img_file)
            if not safe:
                flash(img_reason, 'error')
                return redirect(url_for('characters.edit_character', char_id=char_id))
            new_av = save_upload(img_file, 'avatars')
            if new_av: av = new_av
        db.execute('UPDATE characters SET name=%s,race=%s,class=%s,trait1=%s,trait2=%s,trait3=%s,backstory=%s,avatar_url=%s WHERE id=%s',
                   (n, race, cls, t1, t2, t3, bs, av, char_id))
        flash('{} updated!'.format(n), 'success')
        return redirect(url_for('characters.character_pool'))
    return render_template('edit_character.html', char=char, traits=CHARACTER_TRAITS,
                           preset_avatars=PRESET_AVATARS, races=CHARACTER_RACES,
                           race_labels=CHARACTER_RACE_LABELS, classes=CHARACTER_CLASSES)


@bp.route('/character/<char_id>/delete', methods=['POST'])
@login_required
def delete_character(char_id):
    db = get_db()
    char = db.fetchone('SELECT * FROM characters WHERE id = %s AND user_id = %s', (char_id, session['user_id']))
    if not char: return redirect(url_for('characters.character_pool'))
    cnt = db.fetchone('SELECT COUNT(*) as c FROM characters WHERE user_id = %s', (session['user_id'],))
    if cnt['c'] <= 1:
        flash('Cannot delete your only character!', 'error')
        return redirect(url_for('characters.character_pool'))
    was_main = char['is_main']
    db.execute('DELETE FROM characters WHERE id = %s', (char_id,))
    if was_main:
        nxt = db.fetchone('SELECT id,name FROM characters WHERE user_id = %s ORDER BY created_at LIMIT 1', (session['user_id'],))
        if nxt:
            db.execute('UPDATE characters SET is_main = 1 WHERE id = %s', (nxt['id'],))
            db.execute('UPDATE users SET main_character_id = %s WHERE id = %s', (nxt['id'], session['user_id']))
    flash('{} removed.'.format(char['name']), 'info')
    return redirect(url_for('characters.character_pool'))
