#!/usr/bin/env python3
"""
Promote a user to admin or revoke admin privileges.

Usage:
    python promote_admin.py <username>              # Promote to admin
    python promote_admin.py <username> --revoke     # Revoke admin
    python promote_admin.py --list                  # List all admins

Run this from the project directory (or on Railway via `railway run python promote_admin.py <username>`).
"""
import sys
import os

# Ensure the project root is in the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from database import get_db, close_db

def main():
    if len(sys.argv) < 2:
        print("Usage: python promote_admin.py <username> [--revoke]")
        print("       python promote_admin.py --list")
        sys.exit(1)

    with app.app_context():
        db = get_db()

        if sys.argv[1] == '--list':
            admins = db.fetchall('SELECT username, email, joined_at FROM users WHERE is_admin = 1')
            if admins:
                print(f"\n🛡️  Admin accounts ({len(admins)}):")
                for a in admins:
                    print(f"   @{a['username']} ({a['email']}) — joined {a['joined_at']}")
            else:
                print("\n⚠️  No admin accounts found. Promote one with:")
                print("   python promote_admin.py <username>")
            close_db()
            return

        username = sys.argv[1]
        revoke = '--revoke' in sys.argv

        user = db.fetchone('SELECT id, username, email, is_admin FROM users WHERE username = %s', (username,))
        if not user:
            print(f"\n❌ User @{username} not found.")
            close_db()
            sys.exit(1)

        if revoke:
            if not user.get('is_admin'):
                print(f"\n⚠️  @{username} is not an admin.")
            else:
                db.execute('UPDATE users SET is_admin = 0 WHERE id = %s', (user['id'],))
                print(f"\n✅ Revoked admin privileges from @{username}.")
        else:
            if user.get('is_admin'):
                print(f"\n⚠️  @{username} is already an admin.")
            else:
                db.execute('UPDATE users SET is_admin = 1 WHERE id = %s', (user['id'],))
                print(f"\n✅ Promoted @{username} to admin!")
                print(f"   They can now access /admin in the app.")

        close_db()

if __name__ == '__main__':
    main()
