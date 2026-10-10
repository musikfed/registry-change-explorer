"""SQLite storage for the local registry index."""

import sqlite3
import threading


class DatabaseManager:
    def __init__(self, db_path='registry.db', timeout=30):
        self.db_path = db_path
        self.timeout = timeout
        self._local = threading.local()

    def connect(self):
        """Return a connection that is private to the current thread."""
        conn = getattr(self._local, 'conn', None)
        if conn is None:
            conn = sqlite3.connect(self.db_path, timeout=self.timeout)
            conn.row_factory = sqlite3.Row
            conn.execute('PRAGMA journal_mode=WAL')
            conn.execute('PRAGMA synchronous=NORMAL')
            self._local.conn = conn
        return conn

    def close(self):
        conn = getattr(self._local, 'conn', None)
        if conn is not None:
            try:
                conn.close()
            finally:
                self._local.conn = None

    def init_database(self):
        """Create or repair the schema idempotently."""
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registry_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                parent_path TEXT NOT NULL,
                hive TEXT NOT NULL,
                depth INTEGER NOT NULL DEFAULT 0,
                has_children INTEGER NOT NULL DEFAULT 0,
                values_count INTEGER NOT NULL DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registry_values (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key_path TEXT NOT NULL,
                name TEXT NOT NULL,
                type_code INTEGER NOT NULL,
                type_name TEXT NOT NULL,
                data TEXT NOT NULL DEFAULT '',
                size INTEGER NOT NULL DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registry_metadata (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('CREATE INDEX IF NOT EXISTS idx_keys_parent ON registry_keys(parent_path)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_keys_name ON registry_keys(name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_values_key ON registry_values(key_path)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_values_name ON registry_values(name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_values_data ON registry_values(data)')
        conn.commit()
        self.close()
        return True

    def get_stats(self):
        self.init_database()
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM registry_keys')
        keys = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM registry_values')
        values = cursor.fetchone()[0]
        cursor.execute('SELECT value FROM registry_metadata WHERE key = ?', ('last_sync',))
        row = cursor.fetchone()
        last_sync = row['value'] if row and row['value'] else 'никогда'
        self.close()
        return {
            'total_keys': keys,
            'total_values': values,
            'last_sync': last_sync,
        }
