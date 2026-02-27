"""
Seed script — Demo data with campaign, story, and art posts.
Run: python seed.py
"""
import uuid, json
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from app import app
from database import get_db, init_db

USERS = [
    {'username':'grimthorn','email':'grim@example.com','password':'demo123',
     'characters':[
         {'name':'Grimthorn the Grey','race':'Human','class':'Wizard','trait1':'Scholarly','trait2':'Enigmatic','trait3':'Sardonic','is_main':True,
          'backstory':'Born in Valdris to a family of shipwrights, Grimthorn showed an aptitude for the arcane at age seven when he accidentally set the workshop ablaze with a sneeze. Now the reluctant Archmage, he would rather be reading than attending council meetings.'},
         {'name':'Ashwick the Humble','race':'Human','class':'Druid','trait1':'Compassionate','trait2':'Wise','trait3':'Melancholic','is_main':False,
          'backstory':'Grimthorn\'s alter ego for traveling incognito. A wandering hedge wizard who helps villagers for nothing but a warm meal.'},
     ]},
    {'username':'lyraswift','email':'lyra@example.com','password':'demo123',
     'characters':[
         {'name':'Lyra Swiftarrow','race':'Elf','class':'Ranger','trait1':'Perceptive','trait2':'Nature-Bound','trait3':'Rebellious','is_main':True,
          'backstory':'Half-elf ranger raised in Verdantholm. She learned to track before she could read and outshoot the village elders by twelve. Now a Warden of the Wild, protecting the Thornwood.'},
     ]},
    {'username':'durgok','email':'durgok@example.com','password':'demo123',
     'characters':[
         {'name':'Durgok Ironbelly','race':'Pkoyte','class':'Warrior','trait1':'Fearless','trait2':'Jovial','trait3':'Loyal','is_main':True,
          'backstory':'Born in a gladiatorial pit — literally. His mother went into labor mid-fight and still won. Durgok\'s true passion is culinary arts. His Owlbear Stew makes dwarves weep with joy.'},
     ]},
    {'username':'whisper','email':'whisper@example.com','password':'demo123',
     'characters':[
         {'name':'Whisper','race':'Karagonian','class':'Rogue','trait1':'Deceptive','trait2':'Cunning','trait3':'Haunted','is_main':True,
          'backstory':'Nobody knows Whisper\'s real name. A tiefling rogue who appeared in Duskhollow fifteen years ago with an unsettling ability to know things they shouldn\'t.'},
     ]},
    {'username':'bramblewise','email':'bramble@example.com','password':'demo123',
     'characters':[
         {'name':'Bramblewise','race':'Winterman','class':'Druid','trait1':'Serene','trait2':'Eccentric','trait3':'Nature-Bound','is_main':True,
          'backstory':'A firbolg druid who has lived in the Whispering Grove for longer than most kingdoms have existed. Terrifyingly powerful when roused.'},
     ]},
]

POSTS = [
    # CAMPAIGN post
    {'author':'grimthorn','post_type':'campaign','title':'The Fall of Blackthorn Keep',
     'tag_location':'Blackthorn Keep','tag_age':'The Age of Long Knives','tag_characters':'Grimthorn the Grey, Lyra Swiftarrow, Durgok Ironbelly',
     'tagged_users':'lyraswift, durgok','hours_ago':3,
     'sessions':[
         {'title':'The Gathering Storm','content':'We received word that Blackthorn Keep had fallen to a mysterious force. The party assembled at the Silver Tower — Grimthorn reluctantly left his library, Lyra arrived with Professor Hoot, and Durgok brought provisions (and his axe). We set out at dawn.'},
         {'title':'Into the Thornwood','content':'The forest was eerily silent. Lyra tracked strange footprints — humanoid but wrong somehow. We found an abandoned camp with maps of the keep\'s defenses. Someone had been planning this for months.'},
         {'title':'The Siege','content':'We arrived to find the keep surrounded by shadow creatures. Grimthorn identified them as wraiths bound by necromantic chains. Durgok wanted to charge. Lyra wanted to scout. We compromised: Durgok charged while Lyra scouted.'},
     ]},
    # STORY post
    {'author':'whisper','post_type':'story','title':'The Merchant\'s Bargain',
     'content':'The merchant smiled too wide. That was the first warning.\n\nWhisper had seen many deals go wrong in the Sunken Bazaar, but this one had a particular stench of doom about it. Five hundred gold for a "small package" delivered to the Shadowfell. The package hummed.\n\n"Don\'t open it," the merchant said, still smiling. "Don\'t speak to it. And whatever you do, don\'t let it see moonlight."\n\nWhisper took the job. Of course they did. Because sometimes the worst decisions make the best stories.\n\nThree days later, standing at the Shadowfell Gate with a humming box and a growing sense of regret, Whisper finally understood what the merchant had really been selling: not a delivery service, but a sacrifice.',
     'tag_location':'The Sunken Bazaar','tag_age':'The Current Age — The Reckoning','tag_characters':'Whisper, Rattleclaw',
     'tagged_users':'','hours_ago':8},
    # ART post
    {'author':'lyraswift','post_type':'art','title':'Map of the Thornwood',
     'description':'Hand-drawn map of the Thornwood Forest showing the Warden patrol routes, the displacer beast nesting grounds, and the location of the abandoned temple we discovered last session. Made this between watches.',
     'tag_location':'Thornwood Forest','tag_age':'The Current Age — The Reckoning','tag_characters':'Lyra Swiftarrow',
     'tagged_users':'','hours_ago':12},
    # STORY post
    {'author':'durgok','post_type':'story','title':'DURGOK\'S RECIPE: Owlbear Stew',
     'content':'DURGOK SHARE SECRET RECIPE!\n\nIngredients:\n- 2 lbs owlbear flank (substitute elk if coward)\n- Wild root vegetables (ask druid which ones)\n- Herbs from the Whispering Grove\n- One splash of dwarven ale\n- Rage seasoning to taste\n\nSlow cook over campfire for 3 hours. Feeds party of 5 or one hungry barbarian.\n\nIMPORTANT: Do NOT let wizard "help" with fire. Last time Grimthorn "helped," camp was on fire. Again.\n\nServe with bread. If no bread, serve with more stew. If no stew, COOK MORE STEW.',
     'tag_location':'Frostspire Mountains','tag_age':'The Age of Iron and Ash','tag_characters':'Durgok Ironbelly, Grimthorn the Grey',
     'tagged_users':'grimthorn','hours_ago':18},
    # CAMPAIGN post
    {'author':'bramblewise','post_type':'campaign','title':'The Ecological Survey of the Hollowed Catacombs',
     'tag_location':'The Hollowed Catacombs','tag_age':'The Age of Echoes','tag_characters':'Bramblewise, Elder Mossbeard',
     'tagged_users':'','hours_ago':24,
     'sessions':[
         {'title':'Initial Assessment','content':'The Verdant Circle commissioned this survey after reports of unusual fungal growth in the upper levels. I descended with my usual equipment: specimen jars, field journal, and a very annoyed badger familiar who wanted no part of this.'},
         {'title':'The Myconid Colony','content':'Discovered a thriving myconid community in the mid-levels. They have established a remarkable symbiotic relationship with the cave lichen. I spent three hours in telepathic communication with their Elder. They are concerned about the adventuring parties disturbing their spore cycles.'},
     ]},
    # STORY post
    {'author':'grimthorn','post_type':'story','title':'A Treatise on the Theoretical Limits of Wish',
     'content':'After three campaigns where Wish went catastrophically wrong, I have compiled my findings.\n\nThe fundamental paradox of Wish is this: the spell grants exactly what you ask for, which is almost never what you actually want. Language is imprecise. Reality is literal.\n\n"I wish for immortality" — granted, you are now a lich.\n"I wish for unlimited power" — granted, you are now a lightning rod.\n"I wish this fight was over" — granted, time skips forward, you are dead.\n\nMy recommendation: use Wish to cast 8th-level spells. Anything more creative is just asking the universe to teach you a lesson about hubris.',
     'tag_location':'The Silver Tower','tag_age':'The Age of Wandering Stars','tag_characters':'Grimthorn the Grey',
     'tagged_users':'','hours_ago':30},
]

def seed():
    with app.app_context():
        db = get_db()
        row = db.fetchone('SELECT COUNT(*) as c FROM users')
        if row and row['c'] > 0:
            print('DB already seeded. Delete poetic_goblin.db first.'); return

        uids = {}
        for u in USERS:
            uid = str(uuid.uuid4()); uids[u['username']] = uid
            db.execute('INSERT INTO users (id,username,email,password_hash,email_verified) VALUES (%s,%s,%s,%s,%s)',
                       (uid, u['username'], u['email'], generate_password_hash(u['password']), 1))
            main_cid = None
            for c in u['characters']:
                cid = str(uuid.uuid4())
                db.execute('INSERT INTO characters (id,user_id,name,race,class,trait1,trait2,trait3,backstory,is_main) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                           (cid, uid, c['name'], c.get('race',''), c.get('class',''), c['trait1'], c['trait2'], c['trait3'], c['backstory'], 1 if c['is_main'] else 0))
                if c['is_main']: main_cid = cid
            if main_cid: db.execute('UPDATE users SET main_character_id=%s WHERE id=%s', (main_cid, uid))

        for p in POSTS:
            pid = str(uuid.uuid4())
            ts = (datetime.now() - timedelta(hours=p['hours_ago'])).strftime('%Y-%m-%d %H:%M:%S')
            db.execute('INSERT INTO posts (id,author_id,post_type,title,description,content,tag_location,tag_age,tag_characters,tagged_users,created_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (pid, uids[p['author']], p['post_type'], p['title'], p.get('description',''), p.get('content',''),
                        p.get('tag_location',''), p.get('tag_age',''), p.get('tag_characters',''), p.get('tagged_users',''), ts))
            if p['post_type'] == 'campaign' and 'sessions' in p:
                for i, s in enumerate(p['sessions']):
                    sid = str(uuid.uuid4())
                    db.execute('INSERT INTO campaign_sessions (id,post_id,session_number,title,content) VALUES (%s,%s,%s,%s,%s)',
                               (sid, pid, i+1, s['title'], s['content']))

        follows = [('lyraswift','grimthorn'),('lyraswift','bramblewise'),('durgok','lyraswift'),
                   ('durgok','whisper'),('whisper','durgok'),('whisper','grimthorn'),
                   ('bramblewise','lyraswift'),('bramblewise','grimthorn'),('grimthorn','bramblewise')]
        for a,b in follows:
            db.execute('INSERT INTO follows (follower_id,followed_id) VALUES (%s,%s)', (uids[a], uids[b]))

        # Demo conversations
        convos = [
            {'between': ('grimthorn', 'lyraswift'), 'messages': [
                ('grimthorn', 'Lyra, I need your tracking skills. Something has been prowling near the Silver Tower at night.', 5),
                ('lyraswift', 'Professor Hoot spotted unusual tracks last week. Large, clawed, four-toed. Not any creature I recognize from the Thornwood.', 4),
                ('grimthorn', 'Four-toed? That narrows it down. I have a tome that catalogs pre-Sundering fauna. Meet me at the Tower library?', 3),
                ('lyraswift', 'Be there at dawn. I\'ll bring Professor Hoot — his night vision is better than mine.', 2),
                ('grimthorn', 'Excellent. And Lyra? Bring your bow. Just in case the "fauna" decides to visit while we\'re reading.', 1),
            ]},
            {'between': ('durgok', 'whisper'), 'messages': [
                ('durgok', 'WHISPER. Durgok need favor.', 8),
                ('whisper', 'Last time you asked for a "favor" I ended up dangling from a chandelier in the Gilded Undercity.', 7),
                ('durgok', 'That was fun! No, this different. Durgok need rare spice for new recipe. Only found in Sunken Bazaar black market.', 6),
                ('whisper', 'You want me to use my underworld contacts... to buy cooking ingredients.', 5),
                ('durgok', 'Yes! Saffron of the Deep. Very rare. Very expensive. Durgok pay!', 4),
                ('whisper', 'I can\'t believe I\'m saying this, but fine. You owe me one stew.', 3),
            ]},
            {'between': ('bramblewise', 'grimthorn'), 'messages': [
                ('bramblewise', 'Grimthorn. The mycelium network beneath the Whispering Grove is agitated. Something stirs in the deep places.', 12),
                ('grimthorn', 'Define "agitated." Are we talking mild tremors or "evacuate the continent" agitated?', 11),
                ('bramblewise', 'The mushrooms are screaming. I have never heard mushrooms scream before, and I have listened to mushrooms for three hundred years.', 10),
                ('grimthorn', 'That is... deeply unsettling. I\'ll consult the sealed archives. Can you keep the Grove stable in the meantime?', 9),
                ('bramblewise', 'I will try. But Grimthorn — the last time the deep places stirred, it was the Hollow. Please hurry.', 8),
            ]},
        ]
        for conv in convos:
            u1, u2 = conv['between']
            conv_id = str(uuid.uuid4())
            db.execute('INSERT INTO conversations (id, user1_id, user2_id) VALUES (%s,%s,%s)',
                       (conv_id, uids[u1], uids[u2]))
            for sender, content, hours_ago in conv['messages']:
                msg_id = str(uuid.uuid4())
                ts = (datetime.now() - timedelta(hours=hours_ago)).strftime('%Y-%m-%d %H:%M:%S')
                db.execute('INSERT INTO messages (id, conversation_id, sender_id, content, is_read, created_at) VALUES (%s,%s,%s,%s,%s,%s)',
                           (msg_id, conv_id, uids[sender], content, 1, ts))
            db.execute('UPDATE conversations SET last_message_at = %s WHERE id = %s',
                       ((datetime.now() - timedelta(hours=conv['messages'][-1][2])).strftime('%Y-%m-%d %H:%M:%S'), conv_id))

        db.commit()
        print(f'Seeded {len(USERS)} users and {len(POSTS)} posts!')
        print('\nDemo accounts (password: demo123):')
        for u in USERS:
            m = [c for c in u['characters'] if c['is_main']][0]
            print(f"  @{u['username']:15s} → {m['name']}")

if __name__ == '__main__':
    seed()
