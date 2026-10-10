"""Registry indexing and search orchestration."""

import threading
import time
from datetime import datetime

from database.manager import DatabaseManager
from core.registry import RegistryLowLevel
from core.demo_data import DEMO_KEYS, DEMO_VALUES


class RegistryExplorer:
    def __init__(self, db_path='registry.db', demo_mode=False):
        self.db = DatabaseManager(db_path)
        self.demo_mode = demo_mode
        self.registry = None if demo_mode else RegistryLowLevel()
        self.is_syncing = False
        self.sync_progress = 0
        self.sync_error = None
        self._initialized = False
        self._state_lock = threading.Lock()

    def _ensure_db(self):
        if not self._initialized:
            self.db.init_database()
            self._initialized = True

    def start_sync(self):
        """Start one background synchronization. Returns False if one is already running."""
        with self._state_lock:
            if self.is_syncing:
                return False
            self.is_syncing = True
            self.sync_progress = 0
            self.sync_error = None

        self._ensure_db()
        thread = threading.Thread(target=self._sync_full, daemon=True, name='registry-sync')
        thread.start()
        return True

    def _sync_full(self):
        started = time.time()
        try:
            if self.demo_mode:
                self._sync_demo()
            else:
                self._sync_windows()
            elapsed = time.time() - started
            print(f'\n✅ Sync complete: {self.sync_progress} keys in {elapsed:.1f}s')
        except Exception as exc:
            self.sync_error = str(exc)
            print(f'\n❌ Sync failed: {exc}')
        finally:
            self.db.close()
            with self._state_lock:
                self.is_syncing = False

    def _prepare_sync(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM registry_values')
        cursor.execute('DELETE FROM registry_keys')
        return conn, cursor

    def _finish_sync(self, conn):
        cursor = conn.cursor()
        cursor.execute(
            'INSERT OR REPLACE INTO registry_metadata (key, value, updated_at) VALUES (?, ?, CURRENT_TIMESTAMP)',
            ('last_sync', datetime.now().isoformat(timespec='seconds')),
        )
        conn.commit()

    def _sync_demo(self):
        conn, cursor = self._prepare_sync()
        child_parents = {row[2] for row in DEMO_KEYS if row[2]}
        value_counts = {}
        for key_path, *_ in DEMO_VALUES:
            value_counts[key_path] = value_counts.get(key_path, 0) + 1

        for path, name, parent, hive, depth in DEMO_KEYS:
            cursor.execute(
                '''INSERT INTO registry_keys
                   (path, name, parent_path, hive, depth, has_children, values_count)
                   VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (path, name, parent, hive, depth, int(path in child_parents), value_counts.get(path, 0)),
            )
            self.sync_progress += 1

        cursor.executemany(
            '''INSERT INTO registry_values
               (key_path, name, type_code, type_name, data, size)
               VALUES (?, ?, ?, ?, ?, ?)''',
            DEMO_VALUES,
        )
        self._finish_sync(conn)

    def _sync_windows(self):
        conn, cursor = self._prepare_sync()

        def process_key(path, depth=0):
            key = self.registry.open_key(path)
            if not key:
                return
            try:
                parts = path.split('\\')
                name = parts[-1]
                parent = '\\'.join(parts[:-1]) if len(parts) > 1 else ''
                hive = parts[0]
                has_children = bool(self.registry.enum_key(key, 0))

                cursor.execute(
                    '''INSERT OR IGNORE INTO registry_keys
                       (path, name, parent_path, hive, depth, has_children)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (path, name, parent, hive, depth, int(has_children)),
                )

                value_count = 0
                index = 0
                while True:
                    value = self.registry.enum_value(key, index)
                    if value is None:
                        break
                    value_name, value_data, type_code = value
                    cursor.execute(
                        '''INSERT INTO registry_values
                           (key_path, name, type_code, type_name, data, size)
                           VALUES (?, ?, ?, ?, ?, ?)''',
                        (
                            path,
                            value_name or '(Default)',
                            type_code,
                            self.registry.get_type_name(type_code),
                            str(self.registry.format_data(value_data, type_code))[:4000],
                            self.registry.calc_size(value_data, type_code),
                        ),
                    )
                    value_count += 1
                    index += 1

                if value_count:
                    cursor.execute(
                        'UPDATE registry_keys SET values_count = ? WHERE path = ?',
                        (value_count, path),
                    )

                index = 0
                while True:
                    subkey = self.registry.enum_key(key, index)
                    if subkey is None:
                        break
                    process_key(f'{path}\\{subkey}', depth + 1)
                    index += 1
            finally:
                try:
                    key.Close()
                except OSError:
                    pass

            self.sync_progress += 1
            if self.sync_progress % 500 == 0:
                conn.commit()
                print(f'\r⏳ Indexed: {self.sync_progress} keys', end='', flush=True)

        for root in ('HKEY_CURRENT_USER', 'HKEY_LOCAL_MACHINE', 'HKEY_CLASSES_ROOT', 'HKEY_USERS', 'HKEY_CURRENT_CONFIG'):
            process_key(root)
        self._finish_sync(conn)

    def get_subkeys(self, path):
        self._ensure_db()
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT path, name, has_children, values_count
               FROM registry_keys WHERE parent_path = ? ORDER BY name COLLATE NOCASE''',
            (path,),
        )
        rows = [
            {
                'path': row['path'],
                'name': row['name'],
                'has_children': bool(row['has_children']),
                'values_count': row['values_count'],
            }
            for row in cursor.fetchall()
        ]
        self.db.close()
        return rows

    def get_values(self, path):
        self._ensure_db()
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT name, type_name, data, type_code, size
               FROM registry_values WHERE key_path = ?
               ORDER BY CASE WHEN name = '(Default)' THEN 0 ELSE 1 END, name COLLATE NOCASE''',
            (path,),
        )
        rows = []
        for row in cursor.fetchall():
            data = row['data'] or ''
            rows.append({
                'name': row['name'],
                'type': row['type_name'],
                'data': data[:500] + ('…' if len(data) > 500 else ''),
                'type_code': row['type_code'],
                'size': row['size'],
            })
        self.db.close()
        return rows

    def search(self, term):
        self._ensure_db()
        query = f'%{term}%'
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT path, name FROM registry_keys
               WHERE name LIKE ? OR path LIKE ?
               ORDER BY path LIMIT 200''',
            (query, query),
        )
        keys = [{'path': row['path'], 'name': row['name'], 'type': 'key'} for row in cursor.fetchall()]
        cursor.execute(
            '''SELECT key_path, name, data, type_name FROM registry_values
               WHERE name LIKE ? OR data LIKE ?
               ORDER BY key_path, name LIMIT 200''',
            (query, query),
        )
        values = [
            {
                'path': row['key_path'],
                'name': row['name'],
                'data': (row['data'] or '')[:140],
                'type': row['type_name'],
            }
            for row in cursor.fetchall()
        ]
        self.db.close()
        return {'keys': keys, 'values': values, 'total': len(keys) + len(values)}

    def get_stats(self):
        self._ensure_db()
        stats = self.db.get_stats()
        stats.update({
            'is_syncing': self.is_syncing,
            'progress': self.sync_progress,
            'error': self.sync_error,
            'demo_mode': self.demo_mode,
        })
        return stats
