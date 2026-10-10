"""Low-level Windows Registry access."""

try:
    import winreg
except ImportError:  # Allows demo mode and docs tooling on non-Windows hosts.
    winreg = None


class RegistryLowLevel:
    """Direct, read-focused access to the Windows Registry."""

    def __init__(self):
        if winreg is None:
            raise RuntimeError(
                'Windows Registry is unavailable on this platform. '
                'Set RCE_DEMO_MODE=1 to run the UI demo.'
            )
        self.hives = {
            'HKEY_CLASSES_ROOT': winreg.HKEY_CLASSES_ROOT,
            'HKEY_CURRENT_USER': winreg.HKEY_CURRENT_USER,
            'HKEY_LOCAL_MACHINE': winreg.HKEY_LOCAL_MACHINE,
            'HKEY_USERS': winreg.HKEY_USERS,
            'HKEY_CURRENT_CONFIG': winreg.HKEY_CURRENT_CONFIG,
        }
        self.type_names = {
            1: 'REG_SZ',
            2: 'REG_EXPAND_SZ',
            3: 'REG_BINARY',
            4: 'REG_DWORD',
            7: 'REG_MULTI_SZ',
            11: 'REG_QWORD',
        }

    def open_key(self, path, access=None):
        access = winreg.KEY_READ if access is None else access
        try:
            parts = path.split('\\')
            hive_name = parts[0]
            sub_path = '\\'.join(parts[1:]) if len(parts) > 1 else ''
            if hive_name not in self.hives:
                return None
            for candidate in (access, access | winreg.KEY_WOW64_64KEY):
                try:
                    return winreg.OpenKey(self.hives[hive_name], sub_path, 0, candidate)
                except OSError:
                    continue
        except (OSError, ValueError):
            pass
        return None

    @staticmethod
    def enum_key(key, index):
        try:
            return winreg.EnumKey(key, index)
        except OSError:
            return None

    @staticmethod
    def enum_value(key, index):
        try:
            return winreg.EnumValue(key, index)
        except OSError:
            return None

    def get_type_name(self, code):
        return self.type_names.get(code, f'UNKNOWN({code})')

    @staticmethod
    def format_data(data, type_code):
        if data is None:
            return ''
        if type_code == 3 and isinstance(data, bytes):
            if len(data) <= 8:
                return ' '.join(f'{b:02X}' for b in data)
            preview = ' '.join(f'{b:02X}' for b in data[:8])
            return f'{preview}... ({len(data)} bytes)'
        if type_code in (4, 11) and isinstance(data, int):
            return f'{data} (0x{data:X})'
        if type_code == 7 and isinstance(data, (list, tuple)):
            return ' ; '.join(map(str, data))
        return str(data)

    @staticmethod
    def calc_size(data, type_code):
        if data is None:
            return 0
        if type_code == 3 and isinstance(data, bytes):
            return len(data)
        if type_code == 7 and isinstance(data, (list, tuple)):
            return sum(len(str(item)) for item in data)
        return len(str(data))
