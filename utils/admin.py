# utils/admin.py
# Проверка прав администратора

import ctypes

def check_admin():
    """Проверка прав администратора"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False