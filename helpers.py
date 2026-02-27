"""
Poetic Goblin — Shared Helpers
Decorators, constants, and utility functions used across blueprints.
"""

import logging
from functools import wraps
from flask import session, redirect, url_for, flash, g
from database import get_db
from moderation import censor_text

logger = logging.getLogger('poetic_goblin')

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
        except Exception as e:
            logger.warning('login_required check failed for user %s: %s', session.get('user_id'), e)
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
        except Exception as e:
            logger.warning('character_required check failed for user %s: %s', session.get('user_id'), e)
            session.clear()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


def get_current_user():
    """Get the current user, cached per request via Flask's g object."""
    if hasattr(g, '_cached_current_user'):
        return g._cached_current_user
    if 'user_id' in session:
        db = get_db()
        try:
            user = db.fetchone('''
                SELECT u.id, u.username, u.email, u.joined_at, u.show_explicit,
                       c.id as char_id, c.name as char_name, c.trait1, c.trait2, c.trait3,
                       c.backstory, c.avatar_url as char_avatar
                FROM users u LEFT JOIN characters c ON c.user_id = u.id AND c.is_main = 1
                WHERE u.id = %s
            ''', (session['user_id'],))
            if user:
                g._cached_current_user = user
                return user
            session.clear()
        except Exception as e:
            logger.warning('get_current_user failed for user %s: %s', session.get('user_id'), e)
            session.clear()
    g._cached_current_user = None
    return None


def escape_like(value):
    """Escape SQL LIKE wildcards (% and _) to prevent injection."""
    return value.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')


def censor_filter(text):
    """Censor profanity unless the current user has enabled show_explicit."""
    if not text:
        return text
    user = get_current_user()
    if user and user.get('show_explicit'):
        return text
    return censor_text(text)
