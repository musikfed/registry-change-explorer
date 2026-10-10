"""Small, synthetic registry tree used for screenshots and cross-platform UI demos."""

DEMO_KEYS = [
    ('HKEY_CURRENT_USER', 'HKEY_CURRENT_USER', '', 'HKEY_CURRENT_USER', 0),
    ('HKEY_CURRENT_USER\\Software', 'Software', 'HKEY_CURRENT_USER', 'HKEY_CURRENT_USER', 1),
    ('HKEY_CURRENT_USER\\Software\\RegistryChangeExplorer', 'RegistryChangeExplorer', 'HKEY_CURRENT_USER\\Software', 'HKEY_CURRENT_USER', 2),
    ('HKEY_CURRENT_USER\\Software\\Microsoft', 'Microsoft', 'HKEY_CURRENT_USER\\Software', 'HKEY_CURRENT_USER', 2),
    ('HKEY_CURRENT_USER\\Software\\Microsoft\\Windows', 'Windows', 'HKEY_CURRENT_USER\\Software\\Microsoft', 'HKEY_CURRENT_USER', 3),
    ('HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion', 'CurrentVersion', 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows', 'HKEY_CURRENT_USER', 4),
    ('HKEY_LOCAL_MACHINE', 'HKEY_LOCAL_MACHINE', '', 'HKEY_LOCAL_MACHINE', 0),
    ('HKEY_LOCAL_MACHINE\\SOFTWARE', 'SOFTWARE', 'HKEY_LOCAL_MACHINE', 'HKEY_LOCAL_MACHINE', 1),
    ('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft', 'Microsoft', 'HKEY_LOCAL_MACHINE\\SOFTWARE', 'HKEY_LOCAL_MACHINE', 2),
    ('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT', 'Windows NT', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft', 'HKEY_LOCAL_MACHINE', 3),
    ('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion', 'CurrentVersion', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT', 'HKEY_LOCAL_MACHINE', 4),
    ('HKEY_CLASSES_ROOT', 'HKEY_CLASSES_ROOT', '', 'HKEY_CLASSES_ROOT', 0),
    ('HKEY_USERS', 'HKEY_USERS', '', 'HKEY_USERS', 0),
    ('HKEY_CURRENT_CONFIG', 'HKEY_CURRENT_CONFIG', '', 'HKEY_CURRENT_CONFIG', 0),
]

DEMO_VALUES = [
    ('HKEY_CURRENT_USER\\Software\\RegistryChangeExplorer', 'Theme', 1, 'REG_SZ', 'Midnight', 8),
    ('HKEY_CURRENT_USER\\Software\\RegistryChangeExplorer', 'FastSearch', 4, 'REG_DWORD', '1 (0x1)', 1),
    ('HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion', 'SamplePath', 2, 'REG_EXPAND_SZ', '%USERPROFILE%\\Documents', 24),
    ('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion', 'ProductName', 1, 'REG_SZ', 'Windows (demo data)', 19),
    ('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion', 'DisplayVersion', 1, 'REG_SZ', 'Demo', 4),
]
