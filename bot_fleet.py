"""
Poetic Goblin — Bot Fleet Testing Script
Creates fake accounts, characters, posts, comments, likes, follows, and DMs
to stress-test the app and surface bugs.

Usage:
    pip install requests
    python bot_fleet.py https://your-app.up.railway.app
    python bot_fleet.py http://localhost:5000

Options:
    --bots 10       Number of bot accounts to create (default: 10)
    --posts 5       Posts per bot (default: 5)
    --chaos         Enable chaos mode: sends malformed data, long strings, special chars
"""

import sys
import time
import random
import string
import re
import argparse
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print("Install requests first: pip install requests")
    sys.exit(1)


# ─── Config ──────────────────────────────────────────────────────────────────

TRAITS = [
    "Fearless", "Ruthless", "Cunning", "Charismatic", "Compassionate",
    "Deceptive", "Stealthy", "Wise", "Honorable", "Feral",
    "Eccentric", "Relentless", "Scholarly", "Inspiring", "Vengeful",
]

RACES = ["Human", "Elf", "Pkoyte", "Hiyalmite", "Karagonian", "Lirzan", "Winterman", "Pridekin"]
CLASSES = ["Warrior", "Rogue", "Ranger", "Paladin", "Cleric", "Wizard", "Warlock", "Sorcerer", "Monk", "Druid", "Bard"]

LOCATIONS = [
    "The Shattered Coast", "Valdris, City of Tides", "Thornwood Forest",
    "Duskhollow", "Kragmore Arena", "Frostspire Mountains", "Embervault Citadel",
]

AGES = [
    "The Age of First Light", "The Age of Burning Seas", "The Dragonfall Era",
    "The Age of Echoes", "The Current Age — The Reckoning",
]

PRESET_AVATARS = [
    "/static/avatars/avatar_warrior.svg",
    "/static/avatars/avatar_mage.svg",
    "/static/avatars/avatar_rogue.svg",
    "/static/avatars/avatar_elf.svg",
    "/static/avatars/avatar_ranger.svg",
    "/static/avatars/avatar_bard.svg",
    "/static/avatars/avatar_paladin.svg",
    "/static/avatars/avatar_necromancer.svg",
]

STORY_CONTENT = [
    "The mist rolled through the valley like a living thing, curling around the ankles of our party as we pushed deeper into the Thornwood. Our ranger, ever vigilant, raised a fist — the signal to halt. Something was watching us from the canopy above.",
    "I remember the day the Silver Tower fell. We were camped by the river, sharing stories of better times, when the sky turned the color of bruised plums. The explosion came moments later — a column of light that split the heavens and shook the earth beneath our feet.",
    "The tavern keeper slid the ale across the counter with a knowing look. 'You're the ones asking about the Hollowed Catacombs, aren't you?' He leaned in close. 'Last group that went down there came back with fewer members and more nightmares than they left with.'",
    "My character, Threnody the Unspoken, has walked these lands for longer than most kingdoms have existed. She remembers when the Crimson Sands were green fields, and the Whispering Grove was silent. Time changes everything — except the hunger of the Abyss.",
    "Session 47 was WILD. Our barbarian tried to suplex a dragon. The DM made him roll for it. Natural 20. We lost our minds. The dragon was not amused, but respect was earned that day in Kragmore Arena.",
    "The Pale Dancer appeared at the crossroads at midnight, exactly as the legends foretold. Her offer was simple — a wish granted, a price unnamed. Our warlock stepped forward before anyone could stop them. The deal was struck in silence.",
]

CAMPAIGN_SESSIONS = [
    {"title": "The Road to Duskhollow", "content": "Our party assembled at the Wandering Minstrel tavern. After introductions and a bar fight (naturally), we accepted a contract to investigate disappearances near Duskhollow."},
    {"title": "Into the Dark", "content": "We descended into the ruins beneath the village. Traps, undead, and a mysterious altar awaited. Our cleric identified the symbols as belonging to a forgotten god."},
    {"title": "The Hollow King's Court", "content": "We found the source of the disappearances — the Hollow King himself, raising the dead to rebuild his court. Combat ensued. Two party members went down before we shattered his phylactery."},
    {"title": "Aftermath and Rewards", "content": "Duskhollow was saved. The mayor rewarded us handsomely. But our warlock pocketed a shard of the phylactery when no one was looking... setting up our next arc."},
]

COMMENTS = [
    "This is incredible! Love the detail in your storytelling.",
    "Our party had a similar encounter in the Thornwood — barely made it out alive!",
    "Your character sounds amazing. Would love to see them in a campaign.",
    "The Hollow King arc sounds epic. How many sessions did it span?",
    "I wish my DM was this creative. Great write-up!",
    "Saving this for inspiration for my next session.",
    "The worldbuilding here is chef's kiss.",
    "That natural 20 moment is what D&D is all about!",
    "Beautiful artwork! What tools did you use?",
    "Following for more adventures from your party.",
]

DM_MESSAGES = [
    "Hey! Loved your latest post. Would you be interested in joining our campaign?",
    "Your character's backstory is so cool. How long have you been playing?",
    "We're looking for a {} for our group. Interested?",
    "Just wanted to say your contributions to the Annals are amazing!",
    "Have you explored the Frostspire Mountains arc? It's wild.",
    "GG on that session recap. Our party is doing something similar!",
    "Welcome to Poetic Goblin! Let me know if you need any help getting started.",
    "Would you want to collaborate on a story set in the Shattered Coast?",
]

ANNALS_TITLES = [
    "The Fall of the Crystal Spire",
    "When Dragons Walked as Men",
    "The Merchant's Betrayal at Valdris",
    "Lost Songs of the Whispering Grove",
    "The Last Stand at Embervault",
]

ANNALS_CONTENT = [
    "In the third century of this age, a great calamity befell the northern reaches. The Crystal Spire, once a beacon of arcane knowledge, shattered under the weight of forbidden experiments. Scholars who survived spoke of a rift that opened in the foundations — a tear in the fabric of reality that pulsed with eldritch energy. The resulting explosion could be seen from Valdris, and the magical fallout rendered the surrounding lands uninhabitable for decades to come.",
    "Few remember the time when the great wyrms walked among mortals in disguise. They took the forms of merchants, scholars, and even kings. Their motivations were as varied as their scales — some sought to guide civilization, others to exploit it. The Dragonfall Era takes its name from the moment their masquerade was discovered and the terrible war that followed.",
]


# ─── Bot Class ───────────────────────────────────────────────────────────────

class Bot:
    def __init__(self, base_url, bot_num, chaos=False):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.bot_num = bot_num
        self.chaos = chaos
        self.username = f"testbot_{bot_num}_{random.randint(1000, 9999)}"
        self.email = f"{self.username}@test.poeticgoblin.dev"
        self.password = f"TestPass{bot_num}!"
        self.char_name = random.choice([
            "Aelindra", "Brogmir", "Caelis", "Drekka", "Elyndor",
            "Faelan", "Grimmjaw", "Halvard", "Ilyris", "Jorvak",
            "Kethara", "Luthien", "Mordecai", "Nyxara", "Orinvald",
        ]) + f" the Bot-{bot_num}"
        self.post_ids = []
        self.errors = []
        self.successes = 0

    def url(self, path):
        return urljoin(self.base_url + '/', path.lstrip('/'))

    def _safe_request(self, method, url, action, **kwargs):
        """Make an HTTP request with retry and connection error handling."""
        for attempt in range(3):
            try:
                if method == 'GET':
                    return self.session.get(url, timeout=30, **kwargs)
                else:
                    return self.session.post(url, timeout=30, **kwargs)
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
                if attempt < 2:
                    time.sleep(1 * (attempt + 1))  # Back off: 1s, 2s
                    continue
                self.errors.append(f"[{self.username}] {action}: Connection failed after 3 attempts")
                return None
        return None

    def _get_csrf(self, html):
        """Extract CSRF token from page HTML."""
        match = re.search(r'name="_csrf_token"\s+value="([^"]+)"', html)
        if match:
            return match.group(1)
        match = re.search(r'name="csrf-token"\s+content="([^"]+)"', html)
        if match:
            return match.group(1)
        return ''

    def _check(self, resp, action, expect_codes=(200, 302)):
        """Check response and log errors."""
        if resp is None:
            return False
        if resp.status_code not in expect_codes:
            self.errors.append(f"[{self.username}] {action}: HTTP {resp.status_code}")
            return False
        # Check for error flash messages in response
        if resp.status_code == 200 and 'flash-error' in resp.text:
            error_match = re.search(r'flash-error[^>]*>([^<]+)', resp.text)
            err_text = error_match.group(1).strip() if error_match else 'unknown error'
            self.errors.append(f"[{self.username}] {action}: Flash error — {err_text}")
            return False
        self.successes += 1
        return True

    # ─── Actions ──────────────────────────────────────────────────────

    def register(self):
        """Create an account."""
        resp = self._safe_request('GET', self.url('/register'), 'register')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        data = {
            '_csrf_token': csrf,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'confirm_password': self.password,
        }
        resp = self._safe_request('POST', self.url('/register'), 'register', data=data, allow_redirects=True)
        return self._check(resp, 'register')

    def create_character(self):
        """Create a character."""
        resp = self._safe_request('GET', self.url('/character/create'), 'create_character')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        traits = random.sample(TRAITS, 3)
        data = {
            '_csrf_token': csrf,
            'char_name': self.char_name,
            'char_race': random.choice(RACES),
            'char_class': random.choice(CLASSES),
            'trait1': traits[0],
            'trait2': traits[1],
            'trait3': traits[2],
            'backstory': f"Born in the shadows of {random.choice(LOCATIONS)}, {self.char_name} has walked a path few dare to tread. Their journey began when fate intervened...",
            'preset_avatar': random.choice(PRESET_AVATARS),
        }
        resp = self._safe_request('POST', self.url('/character/create'), 'create_character', data=data, allow_redirects=True)
        return self._check(resp, 'create_character')

    def create_story_post(self):
        """Create a story post."""
        resp = self._safe_request('GET', self.url('/post/create'), 'create_story_post')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        data = {
            '_csrf_token': csrf,
            'post_type': 'story',
            'title': random.choice([
                "A Night in the Thornwood",
                "The Battle of Kragmore",
                "Whispers from the Deep",
                "My First Campaign — A Retrospective",
                "The Merchant's Gambit",
                "When the Stars Went Dark",
                "Tales from Session Zero",
            ]) + f" (Bot {self.bot_num})",
            'content': random.choice(STORY_CONTENT),
            'tag_location': random.choice(LOCATIONS + ['']),
            'tag_age': random.choice(AGES + ['']),
            'tag_characters': '',
            'tagged_users': '',
        }
        resp = self._safe_request('POST', self.url('/post/create'), 'create_story_post', data=data, allow_redirects=True)
        ok = self._check(resp, 'create_story_post')
        if ok:
            # Extract post IDs from the feed page (UUIDs only, not /post/create)
            matches = re.findall(r'/post/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})', resp.text)
            if matches and matches[0] not in self.post_ids:
                self.post_ids.append(matches[0])
        return ok

    def create_campaign_post(self):
        """Create a campaign post with sessions."""
        resp = self._safe_request('GET', self.url('/post/create'), 'create_campaign_post')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        import json
        num_sessions = random.randint(1, 4)
        sessions = CAMPAIGN_SESSIONS[:num_sessions]
        data = {
            '_csrf_token': csrf,
            'post_type': 'campaign',
            'title': f"Campaign: The {random.choice(['Lost', 'Forgotten', 'Cursed', 'Hidden', 'Ancient'])} {random.choice(['Tomb', 'Tower', 'Forest', 'Kingdom', 'Relic'])} (Bot {self.bot_num})",
            'sessions_data': json.dumps(sessions),
            'tag_location': random.choice(LOCATIONS + ['']),
            'tag_age': random.choice(AGES + ['']),
            'tag_characters': '',
            'tagged_users': '',
        }
        resp = self._safe_request('POST', self.url('/post/create'), 'create_campaign_post', data=data, allow_redirects=True)
        ok = self._check(resp, 'create_campaign_post')
        if ok:
            matches = re.findall(r'/post/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})', resp.text)
            if matches and matches[0] not in self.post_ids:
                self.post_ids.append(matches[0])
        return ok

    def like_post(self, post_id):
        """Like a post via AJAX."""
        resp = self._safe_request('GET', self.url('/feed'), 'like_post')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        resp = self._safe_request('POST',
            self.url(f'/post/{post_id}/like'),
            f'like_post({post_id[:8]}...)',
            headers={'X-Requested-With': 'XMLHttpRequest', 'X-CSRF-Token': csrf},
        )
        return self._check(resp, f'like_post({post_id[:8]}...)')

    def comment_on_post(self, post_id):
        """Comment on a post via AJAX."""
        resp = self._safe_request('GET', self.url('/feed'), 'comment')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        resp = self._safe_request('POST',
            self.url(f'/post/{post_id}/comment'),
            f'comment({post_id[:8]}...)',
            data={'content': random.choice(COMMENTS)},
            headers={'X-Requested-With': 'XMLHttpRequest', 'X-CSRF-Token': csrf},
        )
        return self._check(resp, f'comment({post_id[:8]}...)')

    def follow_user(self, username):
        """Follow another user via AJAX."""
        resp = self._safe_request('GET', self.url('/feed'), 'follow')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        resp = self._safe_request('POST',
            self.url(f'/follow/{username}'),
            f'follow({username})',
            headers={'X-Requested-With': 'XMLHttpRequest', 'X-CSRF-Token': csrf},
        )
        return self._check(resp, f'follow({username})')

    def send_dm(self, username):
        """Send a direct message via AJAX."""
        resp = self._safe_request('GET', self.url(f'/messages/{username}'), f'send_dm({username})')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        msg = random.choice(DM_MESSAGES).format(random.choice(CLASSES))
        resp = self._safe_request('POST',
            self.url(f'/messages/{username}/send'),
            f'send_dm({username})',
            data={'content': msg},
            headers={'X-Requested-With': 'XMLHttpRequest', 'X-CSRF-Token': csrf},
        )
        return self._check(resp, f'send_dm({username})')

    def browse_feed(self):
        """Browse the feed."""
        resp = self._safe_request('GET', self.url('/feed'), 'browse_feed')
        return self._check(resp, 'browse_feed')

    def browse_explore(self):
        """Browse explore page."""
        resp = self._safe_request('GET', self.url('/explore'), 'browse_explore')
        return self._check(resp, 'browse_explore')

    def browse_annals(self):
        """Browse the Annals."""
        resp = self._safe_request('GET', self.url('/annals'), 'browse_annals')
        return self._check(resp, 'browse_annals')

    def search(self, query):
        """Search the feed."""
        resp = self._safe_request('GET', self.url('/feed'), f'search("{query}")', params={'q': query})
        return self._check(resp, f'search("{query}")')

    def view_profile(self, username):
        """View a user profile."""
        resp = self._safe_request('GET', self.url(f'/profile/{username}'), f'view_profile({username})')
        return self._check(resp, f'view_profile({username})')

    def contribute_annals(self):
        """Submit a story to the Annals."""
        resp = self._safe_request('GET', self.url('/annals/contribute'), 'contribute_annals')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        data = {
            '_csrf_token': csrf,
            'age_number': random.randint(1, 8),
            'century_number': random.randint(1, 10),
            'title': random.choice(ANNALS_TITLES) + f" ({self.username})",
            'content': random.choice(ANNALS_CONTENT),
        }
        resp = self._safe_request('POST', self.url('/annals/contribute'), 'contribute_annals', data=data, allow_redirects=True)
        return self._check(resp, 'contribute_annals')

    # ─── Chaos Mode Tests ─────────────────────────────────────────────

    def chaos_long_content(self):
        """Try submitting extremely long content."""
        resp = self._safe_request('GET', self.url('/post/create'), 'chaos_long_content')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        data = {
            '_csrf_token': csrf,
            'post_type': 'story',
            'title': 'A' * 500,  # Way over typical limits
            'content': 'B' * 50000,  # Very long content
            'tag_location': '',
            'tag_age': '',
            'tag_characters': '',
            'tagged_users': '',
        }
        resp = self._safe_request('POST', self.url('/post/create'), 'chaos_long_content', data=data, allow_redirects=True)
        if not resp:
            return False
        # We expect this to either work or fail gracefully (not 500)
        if resp.status_code == 500:
            self.errors.append(f"[{self.username}] chaos_long_content: SERVER ERROR 500")
            return False
        self.successes += 1
        return True

    def chaos_special_chars(self):
        """Try content with special characters, HTML, SQL-like strings."""
        evil_strings = [
            '<script>alert("xss")</script>',
            "'; DROP TABLE users; --",
            '"><img src=x onerror=alert(1)>',
            "{{7*7}}",
            "${7*7}",
            "Robert'); DROP TABLE students;--",
            "\x00\x01\x02\x03",  # Null bytes
            "🧌" * 100,  # Lots of emoji
            "A" + "\u0300" * 50,  # Unicode combining characters
        ]
        resp = self._safe_request('GET', self.url('/post/create'), 'chaos_special_chars')
        if not resp: return False
        csrf = self._get_csrf(resp.text)
        evil = random.choice(evil_strings)
        data = {
            '_csrf_token': csrf,
            'post_type': 'story',
            'title': f'Chaos Test: {evil[:50]}',
            'content': f'Testing special characters: {evil}',
            'tag_location': evil[:100],
            'tag_age': '',
            'tag_characters': evil[:100],
            'tagged_users': '',
        }
        resp = self._safe_request('POST', self.url('/post/create'), 'chaos_special_chars', data=data, allow_redirects=True)
        if not resp:
            return False
        if resp.status_code == 500:
            self.errors.append(f"[{self.username}] chaos_special_chars: SERVER ERROR 500 with input: {evil[:50]}")
            return False
        self.successes += 1
        return True

    def chaos_invalid_ids(self):
        """Try accessing resources with invalid/nonexistent IDs."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        tests = [
            ('/post/' + fake_id, 'fake_post'),
            ('/character/' + fake_id + '/edit', 'fake_char_edit'),
            ('/profile/nonexistent_user_12345', 'fake_profile'),
            ('/messages/nonexistent_user_12345', 'fake_dm'),
            ('/annals/story/' + fake_id, 'fake_annals_story'),
            ('/annals/age/99', 'fake_age'),
            ('/annals/age/1/century/99', 'fake_century'),
            ('/feed?page=-1', 'negative_page'),
            ('/feed?page=999999', 'huge_page'),
            ('/feed?page=abc', 'string_page'),
        ]
        ok = True
        for path, label in tests:
            resp = self._safe_request('GET', self.url(path), f'chaos_invalid_ids({label})')
            if not resp:
                ok = False
                continue
            if resp.status_code == 500:
                self.errors.append(f"[{self.username}] chaos_invalid_ids({label}): SERVER ERROR 500")
                ok = False
            else:
                self.successes += 1
        return ok


# ─── Fleet Runner ────────────────────────────────────────────────────────────

def run_fleet(base_url, num_bots=10, posts_per_bot=5, chaos=False):
    print(f"\n🧌 Poetic Goblin Bot Fleet")
    print(f"   Target:  {base_url}")
    print(f"   Bots:    {num_bots}")
    print(f"   Posts:   {posts_per_bot} per bot")
    print(f"   Chaos:   {'ENABLED' if chaos else 'disabled'}")
    print(f"{'='*60}\n")

    # Verify the site is reachable
    try:
        resp = requests.get(base_url, timeout=10)
        if resp.status_code != 200:
            print(f"⚠️  Site returned {resp.status_code}. Continuing anyway...")
    except Exception as e:
        print(f"❌ Cannot reach {base_url}: {e}")
        return

    bots = [Bot(base_url, i + 1, chaos) for i in range(num_bots)]
    all_errors = []

    # Phase 1: Registration & Character Creation
    print("📝 Phase 1: Registration & Character Creation")
    active_bots = []
    for bot in bots:
        if bot.register():
            print(f"   ✅ {bot.username} registered")
            if bot.create_character():
                print(f"   ✅ {bot.username} created character: {bot.char_name}")
                active_bots.append(bot)
            else:
                print(f"   ❌ {bot.username} failed to create character")
        else:
            print(f"   ❌ {bot.username} failed to register")
        time.sleep(0.3)

    if not active_bots:
        print("\n❌ No bots successfully registered. Check the target URL and try again.")
        return

    print(f"\n   {len(active_bots)}/{num_bots} bots active\n")

    # Phase 2: Create Posts
    print("📜 Phase 2: Creating Posts")
    for bot in active_bots:
        for i in range(posts_per_bot):
            if random.random() < 0.3:
                bot.create_campaign_post()
            else:
                bot.create_story_post()
            time.sleep(0.2)
        print(f"   ✅ {bot.username} created {posts_per_bot} posts ({len(bot.post_ids)} tracked)")

    # Collect all post IDs
    all_post_ids = []
    for bot in active_bots:
        all_post_ids.extend(bot.post_ids)

    # Phase 3: Interactions
    print("\n💬 Phase 3: Interactions (likes, comments, follows, DMs)")
    for bot in active_bots:
        # Like random posts
        for post_id in random.sample(all_post_ids, min(5, len(all_post_ids))):
            bot.like_post(post_id)
            time.sleep(0.3)

        # Comment on random posts
        for post_id in random.sample(all_post_ids, min(3, len(all_post_ids))):
            bot.comment_on_post(post_id)
            time.sleep(0.3)

        # Follow random other bots
        other_bots = [b for b in active_bots if b != bot]
        for other in random.sample(other_bots, min(3, len(other_bots))):
            bot.follow_user(other.username)
            time.sleep(0.3)

        # Send DMs to random bots
        for other in random.sample(other_bots, min(2, len(other_bots))):
            bot.send_dm(other.username)
            time.sleep(0.3)

        print(f"   ✅ {bot.username} interacted")

    # Phase 4: Browsing
    print("\n🔍 Phase 4: Browsing & Search")
    for bot in active_bots:
        bot.browse_feed()
        bot.browse_explore()
        bot.browse_annals()
        bot.search("dragon")
        bot.search("campaign")
        bot.search(bot.char_name)
        for other in random.sample(active_bots, min(2, len(active_bots))):
            bot.view_profile(other.username)
        time.sleep(0.2)
        print(f"   ✅ {bot.username} browsed")

    # Phase 5: Annals Contributions
    print("\n📖 Phase 5: Annals Contributions")
    for bot in active_bots[:5]:  # Just first 5 bots
        bot.contribute_annals()
        time.sleep(0.2)
        print(f"   ✅ {bot.username} contributed to the Annals")

    # Phase 6: Chaos Mode
    if chaos:
        print("\n🔥 Phase 6: Chaos Mode")
        for bot in active_bots:
            bot.chaos_long_content()
            time.sleep(0.5)
            bot.chaos_special_chars()
            time.sleep(0.5)
            bot.chaos_special_chars()
            time.sleep(0.5)
            bot.chaos_invalid_ids()
            time.sleep(0.5)
            print(f"   🔥 {bot.username} ran chaos tests")

    # ─── Report ──────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print("📊 RESULTS")
    print(f"{'='*60}")

    total_successes = sum(b.successes for b in bots)
    total_errors = []
    for b in bots:
        total_errors.extend(b.errors)

    print(f"\n   ✅ Successful actions:  {total_successes}")
    print(f"   ❌ Errors:             {len(total_errors)}")

    if total_errors:
        print(f"\n{'─'*60}")
        print("ERRORS:")
        print(f"{'─'*60}")
        for err in total_errors:
            print(f"   • {err}")
    else:
        print(f"\n   🎉 All tests passed! No errors detected.")

    # Summary by bot
    print(f"\n{'─'*60}")
    print("PER-BOT SUMMARY:")
    print(f"{'─'*60}")
    print(f"   {'Bot':<30} {'OK':>5} {'Err':>5}")
    for bot in bots:
        status = "✅" if not bot.errors else "❌"
        print(f"   {status} {bot.username:<27} {bot.successes:>5} {len(bot.errors):>5}")

    print(f"\n{'='*60}")
    print("   Bot accounts created (for manual cleanup later):")
    for bot in active_bots:
        print(f"   • {bot.username} / {bot.password}")
    print(f"{'='*60}\n")


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Poetic Goblin Bot Fleet Testing')
    parser.add_argument('url', help='Base URL of the app (e.g. https://your-app.up.railway.app)')
    parser.add_argument('--bots', type=int, default=10, help='Number of bots (default: 10)')
    parser.add_argument('--posts', type=int, default=5, help='Posts per bot (default: 5)')
    parser.add_argument('--chaos', action='store_true', help='Enable chaos mode (malformed data, edge cases)')

    args = parser.parse_args()
    run_fleet(args.url, num_bots=args.bots, posts_per_bot=args.posts, chaos=args.chaos)
