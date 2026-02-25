"""
Poetic Goblin — Database Abstraction Layer
Supports SQLite (dev), MySQL (prod), and PostgreSQL (prod) with a unified API.

Usage:
    from database import get_db, init_db
    db = get_db()
    rows = db.execute('SELECT * FROM users WHERE id = %s', (uid,))
    row = db.fetchone('SELECT * FROM users WHERE id = %s', (uid,))
"""
import os
import re
import sqlite3
import uuid
from urllib.parse import urlparse
from flask import g
from config import Config

# ─── Row wrapper to make SQLite rows behave like dicts ────────────────────────

class DictRow(dict):
    """Dict subclass that also supports attribute access and index-based key lookup."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

def _sqlite_row_to_dict(cursor, row):
    """Convert sqlite3.Row to DictRow."""
    return DictRow(zip([col[0] for col in cursor.description], row))

# ─── Database wrapper ─────────────────────────────────────────────────────────

class Database:
    """Unified database interface for SQLite, MySQL, and PostgreSQL."""

    def __init__(self, connection, db_type='sqlite'):
        self._conn = connection
        self._db_type = db_type

    @property
    def connection(self):
        return self._conn

    def _convert_params(self, sql, params):
        """Convert %s placeholders to ? for SQLite."""
        if self._db_type == 'sqlite':
            sql = sql.replace('%s', '?')
        return sql, params

    def execute(self, sql, params=None):
        """Execute a query and return all rows (for SELECT) or lastrowid."""
        sql, params = self._convert_params(sql, params or ())
        if self._db_type in ('mysql', 'postgres'):
            cursor = self._conn.cursor()
            cursor.execute(sql, params)
            if sql.strip().upper().startswith('SELECT') or sql.strip().upper().startswith('SHOW'):
                cols = [desc[0] for desc in cursor.description] if cursor.description else []
                return [DictRow(zip(cols, row)) for row in cursor.fetchall()]
            self._conn.commit()
            return cursor
        else:
            cursor = self._conn.execute(sql, params)
            if sql.strip().upper().startswith('SELECT') or sql.strip().upper().startswith('SHOW'):
                return [DictRow(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            self._conn.commit()
            return cursor

    def fetchone(self, sql, params=None):
        """Execute and return first row or None."""
        rows = self.execute(sql, params)
        if isinstance(rows, list):
            return rows[0] if rows else None
        return None

    def fetchall(self, sql, params=None):
        """Execute and return all rows."""
        rows = self.execute(sql, params)
        return rows if isinstance(rows, list) else []

    def insert(self, sql, params=None):
        """Execute an INSERT and return the cursor/result."""
        sql, params = self._convert_params(sql, params or ())
        if self._db_type in ('mysql', 'postgres'):
            cursor = self._conn.cursor()
            cursor.execute(sql, params)
            self._conn.commit()
            return cursor
        else:
            cursor = self._conn.execute(sql, params)
            self._conn.commit()
            return cursor

    def commit(self):
        self._conn.commit()

    def close(self):
        self._conn.close()


# ─── Connection management ────────────────────────────────────────────────────

def _create_connection():
    """Create a new database connection based on config."""
    db_type = Config.get_db_type()

    # DATABASE_URL takes precedence (common on Railway/Render/Heroku)
    if Config.DATABASE_URL:
        if db_type == 'postgres':
            import psycopg2
            url = Config.DATABASE_URL
            # Fix Heroku-style postgres:// → postgresql://
            if url.startswith('postgres://'):
                url = url.replace('postgres://', 'postgresql://', 1)
            conn = psycopg2.connect(url)
            conn.autocommit = False
            return Database(conn, 'postgres')
        elif db_type == 'mysql':
            import pymysql
            parsed = urlparse(Config.DATABASE_URL)
            conn = pymysql.connect(
                host=parsed.hostname,
                port=parsed.port or 3306,
                user=parsed.username,
                password=parsed.password,
                database=parsed.path.lstrip('/'),
                charset='utf8mb4',
                autocommit=False,
                cursorclass=pymysql.cursors.Cursor,
            )
            return Database(conn, 'mysql')

    if db_type == 'postgres':
        import psycopg2
        conn = psycopg2.connect(
            host=Config.POSTGRES_HOST,
            port=Config.POSTGRES_PORT,
            user=Config.POSTGRES_USER,
            password=Config.POSTGRES_PASSWORD,
            dbname=Config.POSTGRES_DATABASE,
        )
        conn.autocommit = False
        return Database(conn, 'postgres')
    elif db_type == 'mysql':
        import pymysql
        conn = pymysql.connect(
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DATABASE,
            charset='utf8mb4',
            autocommit=False,
            cursorclass=pymysql.cursors.Cursor,
        )
        return Database(conn, 'mysql')
    else:
        conn = sqlite3.connect(Config.SQLITE_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        return Database(conn, 'sqlite')


def get_db():
    """Get the database connection for the current request."""
    if 'db' not in g:
        g.db = _create_connection()
    return g.db


def close_db(exception=None):
    """Close the database connection at end of request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()


# ─── Schema ──────────────────────────────────────────────────────────────────

SCHEMA_VERSION = 9

SQLITE_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS schema_version (version INTEGER);
INSERT INTO schema_version VALUES ({SCHEMA_VERSION});

CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    main_character_id TEXT DEFAULT '',
    email_verified INTEGER DEFAULT 0,
    verification_token TEXT DEFAULT '',
    reset_token TEXT DEFAULT '',
    reset_token_expires TIMESTAMP DEFAULT NULL,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS characters (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    name TEXT NOT NULL,
    race TEXT DEFAULT '',
    class TEXT DEFAULT '',
    trait1 TEXT DEFAULT '',
    trait2 TEXT DEFAULT '',
    trait3 TEXT DEFAULT '',
    backstory TEXT DEFAULT '',
    avatar_url TEXT DEFAULT '',
    is_main INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS posts (
    id TEXT PRIMARY KEY,
    author_id TEXT NOT NULL,
    post_type TEXT NOT NULL DEFAULT 'story',
    title TEXT NOT NULL DEFAULT '',
    description TEXT DEFAULT '',
    content TEXT DEFAULT '',
    image_url TEXT DEFAULT '',
    tag_location TEXT DEFAULT '',
    tag_age TEXT DEFAULT '',
    tag_characters TEXT DEFAULT '',
    tagged_users TEXT DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS campaign_sessions (
    id TEXT PRIMARY KEY,
    post_id TEXT NOT NULL,
    session_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS likes (
    user_id TEXT NOT NULL,
    post_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, post_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS comments (
    id TEXT PRIMARY KEY,
    post_id TEXT NOT NULL,
    author_id TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS follows (
    follower_id TEXT NOT NULL,
    followed_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (follower_id, followed_id),
    FOREIGN KEY (follower_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (followed_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS conversations (
    id TEXT PRIMARY KEY,
    user1_id TEXT NOT NULL,
    user2_id TEXT NOT NULL,
    last_message_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user1_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (user2_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS messages (
    id TEXT PRIMARY KEY,
    conversation_id TEXT NOT NULL,
    sender_id TEXT NOT NULL,
    content TEXT NOT NULL,
    is_read INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE,
    FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS annals_stories (
    id TEXT PRIMARY KEY,
    author_id TEXT NOT NULL,
    age_number INTEGER NOT NULL,
    century_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_posts_author ON posts(author_id);
CREATE INDEX IF NOT EXISTS idx_posts_created ON posts(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_likes_post ON likes(post_id);
CREATE INDEX IF NOT EXISTS idx_comments_post ON comments(post_id);
CREATE INDEX IF NOT EXISTS idx_follows_follower ON follows(follower_id);
CREATE INDEX IF NOT EXISTS idx_follows_followed ON follows(followed_id);
CREATE INDEX IF NOT EXISTS idx_messages_conv ON messages(conversation_id, created_at);
CREATE INDEX IF NOT EXISTS idx_messages_unread ON messages(sender_id, is_read);
CREATE INDEX IF NOT EXISTS idx_conversations_users ON conversations(user1_id, user2_id);
CREATE INDEX IF NOT EXISTS idx_characters_user ON characters(user_id, is_main);
CREATE INDEX IF NOT EXISTS idx_annals_stories_loc ON annals_stories(age_number, century_number);
CREATE TABLE IF NOT EXISTS reports (
    id TEXT PRIMARY KEY,
    reporter_id TEXT NOT NULL,
    reported_type TEXT NOT NULL DEFAULT 'post',
    reported_id TEXT NOT NULL,
    reason TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reporter_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS blocks (
    blocker_id TEXT NOT NULL,
    blocked_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (blocker_id, blocked_id),
    FOREIGN KEY (blocker_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (blocked_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_reports_status ON reports(status);
CREATE INDEX IF NOT EXISTS idx_blocks_blocker ON blocks(blocker_id);
"""

MYSQL_SCHEMA = [
    f"CREATE TABLE IF NOT EXISTS schema_version (version INT) ENGINE=InnoDB",
    f"INSERT INTO schema_version VALUES ({SCHEMA_VERSION})",
    """CREATE TABLE IF NOT EXISTS users (
        id VARCHAR(36) PRIMARY KEY,
        username VARCHAR(30) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        main_character_id VARCHAR(36) DEFAULT '',
        email_verified TINYINT DEFAULT 0,
        verification_token VARCHAR(64) DEFAULT '',
        reset_token VARCHAR(64) DEFAULT '',
        reset_token_expires DATETIME DEFAULT NULL,
        joined_at DATETIME DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS characters (
        id VARCHAR(36) PRIMARY KEY,
        user_id VARCHAR(36) NOT NULL,
        name VARCHAR(50) NOT NULL,
        race VARCHAR(30) DEFAULT '',
        class VARCHAR(30) DEFAULT '',
        trait1 VARCHAR(50) DEFAULT '',
        trait2 VARCHAR(50) DEFAULT '',
        trait3 VARCHAR(50) DEFAULT '',
        backstory TEXT DEFAULT NULL,
        avatar_url VARCHAR(512) DEFAULT '',
        is_main TINYINT DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS posts (
        id VARCHAR(36) PRIMARY KEY,
        author_id VARCHAR(36) NOT NULL,
        post_type VARCHAR(20) NOT NULL DEFAULT 'story',
        title VARCHAR(200) NOT NULL DEFAULT '',
        description TEXT DEFAULT NULL,
        content LONGTEXT DEFAULT NULL,
        image_url VARCHAR(512) DEFAULT '',
        tag_location VARCHAR(200) DEFAULT '',
        tag_age VARCHAR(200) DEFAULT '',
        tag_characters TEXT DEFAULT NULL,
        tagged_users TEXT DEFAULT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS campaign_sessions (
        id VARCHAR(36) PRIMARY KEY,
        post_id VARCHAR(36) NOT NULL,
        session_number INT NOT NULL,
        title VARCHAR(200) NOT NULL,
        content LONGTEXT NOT NULL,
        FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS likes (
        user_id VARCHAR(36) NOT NULL,
        post_id VARCHAR(36) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, post_id),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS comments (
        id VARCHAR(36) PRIMARY KEY,
        post_id VARCHAR(36) NOT NULL,
        author_id VARCHAR(36) NOT NULL,
        content TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
        FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS follows (
        follower_id VARCHAR(36) NOT NULL,
        followed_id VARCHAR(36) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (follower_id, followed_id),
        FOREIGN KEY (follower_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (followed_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS conversations (
        id VARCHAR(36) PRIMARY KEY,
        user1_id VARCHAR(36) NOT NULL,
        user2_id VARCHAR(36) NOT NULL,
        last_message_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user1_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (user2_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS messages (
        id VARCHAR(36) PRIMARY KEY,
        conversation_id VARCHAR(36) NOT NULL,
        sender_id VARCHAR(36) NOT NULL,
        content TEXT NOT NULL,
        is_read TINYINT DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE,
        FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS annals_stories (
        id VARCHAR(36) PRIMARY KEY,
        author_id VARCHAR(36) NOT NULL,
        age_number INT NOT NULL,
        century_number INT NOT NULL,
        title VARCHAR(200) NOT NULL,
        content LONGTEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    "CREATE INDEX IF NOT EXISTS idx_posts_author ON posts(author_id)",
    "CREATE INDEX IF NOT EXISTS idx_posts_created ON posts(created_at DESC)",
    "CREATE INDEX IF NOT EXISTS idx_likes_post ON likes(post_id)",
    "CREATE INDEX IF NOT EXISTS idx_comments_post ON comments(post_id)",
    "CREATE INDEX IF NOT EXISTS idx_follows_follower ON follows(follower_id)",
    "CREATE INDEX IF NOT EXISTS idx_follows_followed ON follows(followed_id)",
    "CREATE INDEX IF NOT EXISTS idx_messages_conv ON messages(conversation_id, created_at)",
    "CREATE INDEX IF NOT EXISTS idx_messages_unread ON messages(sender_id, is_read)",
    "CREATE INDEX IF NOT EXISTS idx_conversations_users ON conversations(user1_id, user2_id)",
    "CREATE INDEX IF NOT EXISTS idx_characters_user ON characters(user_id, is_main)",
    "CREATE INDEX IF NOT EXISTS idx_annals_stories_loc ON annals_stories(age_number, century_number)",
    """CREATE TABLE IF NOT EXISTS reports (
        id VARCHAR(36) PRIMARY KEY,
        reporter_id VARCHAR(36) NOT NULL,
        reported_type VARCHAR(20) NOT NULL DEFAULT 'post',
        reported_id VARCHAR(36) NOT NULL,
        reason TEXT NOT NULL,
        status VARCHAR(20) NOT NULL DEFAULT 'pending',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (reporter_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""",
    """CREATE TABLE IF NOT EXISTS blocks (
        blocker_id VARCHAR(36) NOT NULL,
        blocked_id VARCHAR(36) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (blocker_id, blocked_id),
        FOREIGN KEY (blocker_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (blocked_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB""",
    "CREATE INDEX IF NOT EXISTS idx_reports_status ON reports(status)",
    "CREATE INDEX IF NOT EXISTS idx_blocks_blocker ON blocks(blocker_id)",
]

POSTGRES_SCHEMA = [
    f"CREATE TABLE IF NOT EXISTS schema_version (version INTEGER)",
    f"INSERT INTO schema_version VALUES ({SCHEMA_VERSION})",
    """CREATE TABLE IF NOT EXISTS users (
        id VARCHAR(36) PRIMARY KEY,
        username VARCHAR(30) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        main_character_id VARCHAR(36) DEFAULT '',
        email_verified SMALLINT DEFAULT 0,
        verification_token VARCHAR(64) DEFAULT '',
        reset_token VARCHAR(64) DEFAULT '',
        reset_token_expires TIMESTAMP DEFAULT NULL,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS characters (
        id VARCHAR(36) PRIMARY KEY,
        user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        name VARCHAR(50) NOT NULL,
        race VARCHAR(30) DEFAULT '',
        class VARCHAR(30) DEFAULT '',
        trait1 VARCHAR(50) DEFAULT '',
        trait2 VARCHAR(50) DEFAULT '',
        trait3 VARCHAR(50) DEFAULT '',
        backstory TEXT DEFAULT '',
        avatar_url VARCHAR(512) DEFAULT '',
        is_main SMALLINT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS posts (
        id VARCHAR(36) PRIMARY KEY,
        author_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        post_type VARCHAR(20) NOT NULL DEFAULT 'story',
        title VARCHAR(200) NOT NULL DEFAULT '',
        description TEXT DEFAULT '',
        content TEXT DEFAULT '',
        image_url VARCHAR(512) DEFAULT '',
        tag_location VARCHAR(200) DEFAULT '',
        tag_age VARCHAR(200) DEFAULT '',
        tag_characters TEXT DEFAULT '',
        tagged_users TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS campaign_sessions (
        id VARCHAR(36) PRIMARY KEY,
        post_id VARCHAR(36) NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
        session_number INTEGER NOT NULL,
        title VARCHAR(200) NOT NULL,
        content TEXT NOT NULL
    )""",
    """CREATE TABLE IF NOT EXISTS likes (
        user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        post_id VARCHAR(36) NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, post_id)
    )""",
    """CREATE TABLE IF NOT EXISTS comments (
        id VARCHAR(36) PRIMARY KEY,
        post_id VARCHAR(36) NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
        author_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS follows (
        follower_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        followed_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (follower_id, followed_id)
    )""",
    """CREATE TABLE IF NOT EXISTS conversations (
        id VARCHAR(36) PRIMARY KEY,
        user1_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        user2_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        last_message_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS messages (
        id VARCHAR(36) PRIMARY KEY,
        conversation_id VARCHAR(36) NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
        sender_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        content TEXT NOT NULL,
        is_read SMALLINT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS annals_stories (
        id VARCHAR(36) PRIMARY KEY,
        author_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        age_number INTEGER NOT NULL,
        century_number INTEGER NOT NULL,
        title VARCHAR(200) NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    "CREATE INDEX IF NOT EXISTS idx_posts_author ON posts(author_id)",
    "CREATE INDEX IF NOT EXISTS idx_posts_created ON posts(created_at DESC)",
    "CREATE INDEX IF NOT EXISTS idx_likes_post ON likes(post_id)",
    "CREATE INDEX IF NOT EXISTS idx_comments_post ON comments(post_id)",
    "CREATE INDEX IF NOT EXISTS idx_follows_follower ON follows(follower_id)",
    "CREATE INDEX IF NOT EXISTS idx_follows_followed ON follows(followed_id)",
    "CREATE INDEX IF NOT EXISTS idx_messages_conv ON messages(conversation_id, created_at)",
    "CREATE INDEX IF NOT EXISTS idx_messages_unread ON messages(sender_id, is_read)",
    "CREATE INDEX IF NOT EXISTS idx_conversations_users ON conversations(user1_id, user2_id)",
    "CREATE INDEX IF NOT EXISTS idx_characters_user ON characters(user_id, is_main)",
    "CREATE INDEX IF NOT EXISTS idx_annals_stories_loc ON annals_stories(age_number, century_number)",
    """CREATE TABLE IF NOT EXISTS reports (
        id VARCHAR(36) PRIMARY KEY,
        reporter_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        reported_type VARCHAR(20) NOT NULL DEFAULT 'post',
        reported_id VARCHAR(36) NOT NULL,
        reason TEXT NOT NULL DEFAULT '',
        status VARCHAR(20) NOT NULL DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS blocks (
        blocker_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        blocked_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (blocker_id, blocked_id)
    )""",
    "CREATE INDEX IF NOT EXISTS idx_reports_status ON reports(status)",
    "CREATE INDEX IF NOT EXISTS idx_blocks_blocker ON blocks(blocker_id)",
]


def init_db():
    """Initialize the database schema. Handles migrations and fresh installs."""
    db = get_db()
    db_type = Config.get_db_type()

    if db_type == 'postgres':
        _init_postgres(db)
    elif db_type == 'mysql':
        _init_mysql(db)
    else:
        _init_sqlite(db)


def _migrate(db, db_type, from_version):
    """Run incremental migrations between schema versions."""
    if from_version < 7:
        # v7: Add race and class columns to characters
        try:
            db.execute("ALTER TABLE characters ADD COLUMN race TEXT DEFAULT ''")
            print("[Poetic Goblin] Migration v7: Added 'race' column to characters.")
        except Exception:
            pass  # Column may already exist
        try:
            # 'class' is a reserved word in some DBs; SQLite and Postgres handle it fine as a column name
            if db_type == 'mysql':
                db.execute("ALTER TABLE characters ADD COLUMN `class` VARCHAR(30) DEFAULT ''")
            else:
                db.execute("ALTER TABLE characters ADD COLUMN class TEXT DEFAULT ''")
            print("[Poetic Goblin] Migration v7: Added 'class' column to characters.")
        except Exception:
            pass  # Column may already exist
    if from_version < 8:
        # v8: Add reports and blocks tables
        try:
            if db_type == 'mysql':
                db.execute("""CREATE TABLE IF NOT EXISTS reports (
                    id VARCHAR(36) PRIMARY KEY, reporter_id VARCHAR(36) NOT NULL,
                    reported_type VARCHAR(20) NOT NULL DEFAULT 'post', reported_id VARCHAR(36) NOT NULL,
                    reason TEXT NOT NULL, status VARCHAR(20) NOT NULL DEFAULT 'pending',
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (reporter_id) REFERENCES users(id) ON DELETE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4""")
                db.execute("""CREATE TABLE IF NOT EXISTS blocks (
                    blocker_id VARCHAR(36) NOT NULL, blocked_id VARCHAR(36) NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (blocker_id, blocked_id),
                    FOREIGN KEY (blocker_id) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY (blocked_id) REFERENCES users(id) ON DELETE CASCADE
                ) ENGINE=InnoDB""")
            elif db_type == 'postgres':
                db.execute("""CREATE TABLE IF NOT EXISTS reports (
                    id VARCHAR(36) PRIMARY KEY, reporter_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                    reported_type VARCHAR(20) NOT NULL DEFAULT 'post', reported_id VARCHAR(36) NOT NULL,
                    reason TEXT NOT NULL DEFAULT '', status VARCHAR(20) NOT NULL DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
                db.execute("""CREATE TABLE IF NOT EXISTS blocks (
                    blocker_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                    blocked_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (blocker_id, blocked_id))""")
            else:
                db.execute("""CREATE TABLE IF NOT EXISTS reports (
                    id TEXT PRIMARY KEY, reporter_id TEXT NOT NULL, reported_type TEXT NOT NULL DEFAULT 'post',
                    reported_id TEXT NOT NULL, reason TEXT NOT NULL DEFAULT '', status TEXT NOT NULL DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (reporter_id) REFERENCES users(id) ON DELETE CASCADE)""")
                db.execute("""CREATE TABLE IF NOT EXISTS blocks (
                    blocker_id TEXT NOT NULL, blocked_id TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (blocker_id, blocked_id),
                    FOREIGN KEY (blocker_id) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY (blocked_id) REFERENCES users(id) ON DELETE CASCADE)""")
            db.execute("CREATE INDEX IF NOT EXISTS idx_reports_status ON reports(status)")
            db.execute("CREATE INDEX IF NOT EXISTS idx_blocks_blocker ON blocks(blocker_id)")
            print("[Poetic Goblin] Migration v8: Added reports and blocks tables.")
        except Exception as e:
            print(f"[Poetic Goblin] Migration v8 note: {e}")
    if from_version < 9:
        # v9: Mark all existing accounts as email_verified (they were created before verification was required)
        try:
            result = db.execute('UPDATE users SET email_verified = 1 WHERE email_verified = 0')
            print("[Poetic Goblin] Migration v9: Verified all existing user accounts.")
        except Exception as e:
            print(f"[Poetic Goblin] Migration v9 note: {e}")
    # Update schema version
    try:
        db.execute('UPDATE schema_version SET version = %s', (SCHEMA_VERSION,))
        db.commit()
    except Exception:
        db.commit()


def _init_sqlite(db):
    """Initialize SQLite schema with version check."""
    try:
        v = db.fetchone("SELECT version FROM schema_version")
        if v and v['version'] >= SCHEMA_VERSION:
            return
        if v:
            print(f"[Poetic Goblin] Migrating schema v{v['version']} → v{SCHEMA_VERSION}...")
            _migrate(db, 'sqlite', v['version'])
            return
    except Exception:
        pass

    # Fresh install: drop all tables and rebuild
    for table in ['annals_stories', 'messages', 'conversations', 'campaign_sessions', 'comments',
                  'likes', 'follows', 'posts', 'characters', 'users', 'schema_version']:
        try:
            db.execute(f'DROP TABLE IF EXISTS {table}')
        except Exception:
            pass

    db._conn.executescript(SQLITE_SCHEMA)
    db._conn.commit()
    print(f"[Poetic Goblin] SQLite schema v{SCHEMA_VERSION} initialized.")


def _init_mysql(db):
    """Initialize MySQL schema with version check."""
    try:
        v = db.fetchone("SELECT version FROM schema_version")
        if v and v['version'] >= SCHEMA_VERSION:
            return
        if v:
            print(f"[Poetic Goblin] Migrating MySQL schema v{v['version']} → v{SCHEMA_VERSION}...")
            _migrate(db, 'mysql', v['version'])
            return
        print(f"[Poetic Goblin] Schema outdated. Rebuilding...")
        for table in ['annals_stories', 'messages', 'conversations', 'campaign_sessions', 'comments',
                      'likes', 'follows', 'posts', 'characters', 'users', 'schema_version']:
            db.execute(f'DROP TABLE IF EXISTS {table}')
    except Exception:
        pass

    for stmt in MYSQL_SCHEMA:
        stmt = stmt.strip()
        if stmt:
            db.execute(stmt)
    db.commit()
    print(f"[Poetic Goblin] MySQL schema v{SCHEMA_VERSION} initialized.")


def _init_postgres(db):
    """Initialize PostgreSQL schema with version check."""
    try:
        v = db.fetchone("SELECT version FROM schema_version")
        if v and v['version'] >= SCHEMA_VERSION:
            return
        if v:
            print(f"[Poetic Goblin] Migrating PostgreSQL schema v{v['version']} → v{SCHEMA_VERSION}...")
            _migrate(db, 'postgres', v['version'])
            return
        print(f"[Poetic Goblin] Schema outdated. Rebuilding...")
        for table in ['annals_stories', 'messages', 'conversations', 'campaign_sessions', 'comments',
                      'likes', 'follows', 'posts', 'characters', 'users', 'schema_version']:
            db.execute(f'DROP TABLE IF EXISTS {table} CASCADE')
    except Exception:
        # Table might not exist yet, commit to clear error state
        db.commit()

    for stmt in POSTGRES_SCHEMA:
        stmt = stmt.strip()
        if stmt:
            db.execute(stmt)
    db.commit()
    print(f"[Poetic Goblin] PostgreSQL schema v{SCHEMA_VERSION} initialized.")
