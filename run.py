#!/usr/bin/env python
"""Local entry point for Registry Change Explorer."""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.path.dirname(__file__))


def main():
    demo_mode = os.getenv('RCE_DEMO_MODE', '0').lower() in {'1', 'true', 'yes', 'on'}
    if os.name != 'nt' and not demo_mode:
        print('Registry Change Explorer reads the Windows Registry and normally runs on Windows.')
        print('For a cross-platform UI demo use: RCE_DEMO_MODE=1 python run.py')
        raise SystemExit(2)

    from app.web import app, socketio
    from utils.admin import check_admin

    port = int(os.getenv('PORT', '5000'))
    debug = os.getenv('FLASK_DEBUG', '0').lower() in {'1', 'true', 'yes', 'on'}

    print('=' * 64)
    print('REGISTRY CHANGE EXPLORER — fast Windows Registry navigator')
    print('=' * 64)
    print(f"Mode: {'DEMO' if demo_mode else 'WINDOWS REGISTRY'}")
    print(f"Administrator: {'YES' if check_admin() else 'NO'}")
    print(f'Open: http://127.0.0.1:{port}')
    print('=' * 64)

    socketio.run(
        app,
        host='127.0.0.1',
        port=port,
        debug=debug,
        use_reloader=False,
        allow_unsafe_werkzeug=True,
    )


if __name__ == '__main__':
    main()
