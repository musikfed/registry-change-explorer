import tempfile
import time
import unittest
from pathlib import Path

from core.explorer import RegistryExplorer


class DemoModeTest(unittest.TestCase):
    def test_demo_sync_browse_and_search(self):
        with tempfile.TemporaryDirectory() as tmp:
            db_path = str(Path(tmp) / 'registry.db')
            explorer = RegistryExplorer(db_path=db_path, demo_mode=True)

            self.assertTrue(explorer.start_sync())
            deadline = time.time() + 5
            while explorer.is_syncing and time.time() < deadline:
                time.sleep(0.01)

            stats = explorer.get_stats()
            self.assertFalse(stats['is_syncing'])
            self.assertIsNone(stats['error'])
            self.assertGreater(stats['total_keys'], 0)
            self.assertGreater(stats['total_values'], 0)

            subkeys = explorer.get_subkeys('HKEY_CURRENT_USER')
            self.assertTrue(any(item['name'] == 'Software' for item in subkeys))

            results = explorer.search('Microsoft')
            self.assertGreater(results['total'], 0)


if __name__ == '__main__':
    unittest.main()
