#!/usr/bin/env python3
"""Seed a local test admin account. For development only."""
import sys, os, uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from werkzeug.security import generate_password_hash
from app import app
from database import get_db, close_db

with app.app_context():
    db = get_db()
    existing = db.fetchone("SELECT id FROM users WHERE username = %s", ('paradoxfox',))
    if existing:
        db.execute("UPDATE users SET is_admin = 1 WHERE id = %s", (existing['id'],))
        print("✅ @paradoxfox already exists — promoted to admin.")
    else:
        uid = str(uuid.uuid4())
        db.execute(
            "INSERT INTO users (id, username, email, password_hash, email_verified, is_admin) VALUES (%s,%s,%s,%s,1,1)",
            (uid, 'paradoxfox', 'paradoxfox@local.dev', generate_password_hash('WhoAmI24601'))
        )
        print("✅ Created @paradoxfox (admin) — password: WhoAmI24601")
    close_db()
