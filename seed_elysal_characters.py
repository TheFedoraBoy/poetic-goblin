#!/usr/bin/env python3
"""
Seed the 15 canonical Elysal characters from the Annals into @TheFedoraBoy's character pool.

Run once against your database:
    python seed_elysal_characters.py

Each character gets a race, class, 3 traits, a backstory derived from the Annals,
and a matching preset avatar. They are added as non-main characters so they won't
override TheFedoraBoy's active character.
"""

import uuid
from database import Database
from config import Config

# ─── The 15 Elysal Characters ────────────────────────────────────────────────
# Each profile is built from what the Annals describe about them.

ELYSAL_CHARACTERS = [
    {
        "name": "Hipolyptica",
        "race": "Human",
        "class": "Warrior",
        "trait1": "Fearless",
        "trait2": "Commanding",
        "trait3": "Unyielding",
        "backstory": "A towering Ghenyarian chieftain clad in bearskins who united the warring coastal tribes through diplomacy and the threat of a very large stick. He founded Hipola — the oldest city in the world — and built the first standing army, the first courts of law, and the first roads. Everything that followed was a consequence of decisions he made without knowing what he was starting.",
        "avatar": "/static/avatars/avatar_barbarian.svg",
    },
    {
        "name": "Illiman",
        "race": "Human",
        "class": "Monk",
        "trait1": "Wise",
        "trait2": "Serene",
        "trait3": "Compassionate",
        "backstory": "Born in a nameless Pasav desert town, Illiman walked the world for decades preaching a doctrine of radical simplicity: be kind, forgive, look inward before looking outward. He debated philosophers, refused assassination attempts, and reshaped the moral landscape of an entire continent without ever raising a weapon. His teachings became the foundation of Ceresy.",
        "avatar": "/static/avatars/avatar_monk.svg",
    },
    {
        "name": "Kratikar Klae",
        "race": "Hiyalmite",
        "class": "Bard",
        "trait1": "Scholarly",
        "trait2": "Meticulous",
        "trait3": "Devoted",
        "backstory": "A letterboy at Hejem University who read too much and asked too many questions. At nineteen he left Catcher's Rim with a knapsack and a journal. He returned forty-three years later with six hundred tomes of interviews, sketches, and transcribed scrolls. The Annals — his life's work — are housed in the Library of Spires and continue to grow with contributions from those who believe their piece of the world deserves remembering.",
        "avatar": "/static/avatars/avatar_scholar.svg",
    },
    {
        "name": "Queen Sigrid of Raxone",
        "race": "Human",
        "class": "Paladin",
        "trait1": "Ironwilled",
        "trait2": "Strategic",
        "trait3": "Regal",
        "backstory": "Third child of a dead king, born during a civil war, raised in a fortress that smelled of smoke and wet stone. The throne came to her because her brothers died, and she held it because she was better at ruling than any of them would have been. She reformed the military, tamed the Princes of Rax, and forged Raxone into the most formidable power in northern Fondore.",
        "avatar": "/static/avatars/avatar_knight.svg",
    },
    {
        "name": "Emantine Asaundier",
        "race": "Human",
        "class": "Paladin",
        "trait1": "Honorable",
        "trait2": "Stalwart",
        "trait3": "Chivalrous",
        "backstory": "A young soldier who escaped the Siege of Clarity with a handful of survivors and fled to the Isles of Schvaine. There he founded the Knights of Lambridge and spent years in exile forging them into the force that would return to liberate the Leimlands from Debrear occupation. The code of chivalry he established endured for millennia.",
        "avatar": "/static/avatars/avatar_paladin.svg",
    },
    {
        "name": "Kaed Otticus",
        "race": "Human",
        "class": "Warrior",
        "trait1": "Strategic",
        "trait2": "Relentless",
        "trait3": "Loyal",
        "backstory": "The finest general the Gechann Empire ever produced, and the empire tried to kill him for it. He rose through the legions on merit alone — a rarity in the imperial period — and transformed the Geckish military into the professional army that conquered half the known world. His reward was betrayal by the state he served.",
        "avatar": "/static/avatars/avatar_warrior.svg",
    },
    {
        "name": "Vittoria Medelune",
        "race": "Human",
        "class": "Rogue",
        "trait1": "Cunning",
        "trait2": "Daring",
        "trait3": "Rebellious",
        "backstory": "Ardenese by marriage and Geckish by birth, Vittoria was both hero and victim of the Geckish Civil War. The wife of a Medelune banking scion and daughter of a Boulavar merchant, she navigated the war between reformists and the military establishment and emerged as one of the few figures respected by both sides — though both sides also wanted her dead.",
        "avatar": "/static/avatars/avatar_assassin.svg",
    },
    {
        "name": "Zumaraya the Keeper",
        "race": "Lirzan",
        "class": "Druid",
        "trait1": "Selfless",
        "trait2": "Ancient-Souled",
        "trait3": "Merciful",
        "backstory": "When the Gechann came for the dragonborn, Zumaraya hid the children. She was a dragonborn elder — old enough that the smoke from her nostrils had turned from amber to grey. During the Icrazan Genocide she sheltered hundreds of young Lirzans in volcanic cave networks, preserving a generation that would one day lead the Lirzan Renaissance.",
        "avatar": "/static/avatars/avatar_druid.svg",
    },
    {
        "name": "Kael Frostmane",
        "race": "Winterman",
        "class": "Warrior",
        "trait1": "Fearless",
        "trait2": "Inspiring",
        "trait3": "Primal",
        "backstory": "A clan leader from the central ice plains who united the Wintermen by asking the question they had avoided for a thousand years: what are we waiting for? His unification of Perut sent a tremor through the Sacred Hegemony, because a strong Perut changed the balance of power in the North in ways that no diplomat could manage.",
        "avatar": "/static/avatars/avatar_winterman.svg",
    },
    {
        "name": "Pellae Aymundra",
        "race": "Human",
        "class": "Cleric",
        "trait1": "Kindhearted",
        "trait2": "Visionary",
        "trait3": "Devoted",
        "backstory": "The Library of Spires was built by a woman who could not read. Pellae was a Waydrani refugee displaced by the upheavals of the Fifth Age, blown across the Erezetta to the island of Lipse. She could not read a word of the books she housed, but she understood that knowledge needed a home, and she built one that would outlast every kingdom on Fondore.",
        "avatar": "/static/avatars/avatar_mystic.svg",
    },
    {
        "name": "Ixag Taezantaenns",
        "race": "Lirzan",
        "class": "Rogue",
        "trait1": "Deceptive",
        "trait2": "Sly",
        "trait3": "Unpredictable",
        "backstory": "Not a hero in any conventional sense. He was a Lirzan lizardfolk con artist, smuggler, and occasional murderer whose primary contribution to history was founding the Luschnypp Syndicate — a criminal network that grew from the streets of Capera Cuza into an international shadow empire that outlasted most legitimate governments.",
        "avatar": "/static/avatars/avatar_lizardfolk.svg",
    },
    {
        "name": "Lyssandre Elan",
        "race": "Elf",
        "class": "Wizard",
        "trait1": "Analytical",
        "trait2": "Eloquent",
        "trait3": "Rebellious",
        "backstory": "The most dangerous woman in Fondore, and her weapon was a lecture. Cynthian-born and educated at the University of Oradova, she possessed a mind so sharp her professors found her terrifying. Her philosophical works challenged every assumption about governance, religion, and the relationship between the individual and the state, inspiring revolutions across the continent.",
        "avatar": "/static/avatars/avatar_mage.svg",
    },
    {
        "name": "Tigar Pridestalker",
        "race": "Pridekin",
        "class": "Ranger",
        "trait1": "Feral",
        "trait2": "Relentless",
        "trait3": "Honorable",
        "backstory": "Born with the wrong name. Among the Pridekin, the title 'Pridestalker' was reserved for the elite warriors — hunters who tracked the great predators of the Tzunadaine savannah. Tigar was given the name as a curse and spent his life transforming it into a badge of impossible achievement during the Barren Wars.",
        "avatar": "/static/avatars/avatar_pridekin.svg",
    },
    {
        "name": "Iraya Devuo",
        "race": "Human",
        "class": "Bard",
        "trait1": "Daring",
        "trait2": "Inspiring",
        "trait3": "Rebellious",
        "backstory": "The woman who started the Hyacinth Revolution by singing a folk song in a concert hall did not plan a revolution. She planned to set down her tray. Iraya was a Pervin serving woman — descended from generations of the subjugated underclass — whose single act of defiance sparked the transformation of the western peninsula.",
        "avatar": "/static/avatars/avatar_bard.svg",
    },
    {
        "name": "Kem Kironk",
        "race": "Pkoyte",
        "class": "Ranger",
        "trait1": "Resourceful",
        "trait2": "Eccentric",
        "trait3": "Daring",
        "backstory": "Half Pkoyte and half Hiyalmite — a combination so unusual that most people assumed he was joking. His mother was a Hiyalmite fisherwoman who had traveled to Shoale; his father was a Pkoyte miner. Kem became an adventurer who bridged two cultures that had never thought to meet, and his unlikely journey made him one of the most celebrated heroes of the Fourth Age.",
        "avatar": "/static/avatars/avatar_dwarf.svg",
    },
]

TARGET_USERNAME = "TheFedoraBoy"


def seed():
    db = Database()
    db.connect()

    # Look up the user
    user = db.fetchone("SELECT id FROM users WHERE username = %s", (TARGET_USERNAME,))
    if not user:
        print(f"[ERROR] User @{TARGET_USERNAME} not found in the database.")
        print("Make sure you run this against the correct database and the account exists.")
        db.close()
        return

    user_id = user['id']
    print(f"[OK] Found @{TARGET_USERNAME} (id: {user_id})")

    created = 0
    skipped = 0

    for char in ELYSAL_CHARACTERS:
        # Check if character already exists for this user
        existing = db.fetchone(
            "SELECT id FROM characters WHERE user_id = %s AND name = %s",
            (user_id, char['name'])
        )
        if existing:
            print(f"  [SKIP] {char['name']} — already exists")
            skipped += 1
            continue

        char_id = str(uuid.uuid4())
        db.execute('''
            INSERT INTO characters (id, user_id, name, race, class, trait1, trait2, trait3, backstory, avatar_url, is_main)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)
        ''', (
            char_id, user_id, char['name'], char['race'], char['class'],
            char['trait1'], char['trait2'], char['trait3'],
            char['backstory'], char['avatar']
        ))
        print(f"  [CREATED] {char['name']} — {char['race']} {char['class']} ({char['trait1']}, {char['trait2']}, {char['trait3']})")
        created += 1

    print(f"\nDone! Created {created} characters, skipped {skipped}.")
    db.close()


if __name__ == '__main__':
    seed()
