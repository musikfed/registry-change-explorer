"""Flask routes for Registry Change Explorer."""

import os
import secrets

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO

from app.socket_handlers import register_handlers
from core.explorer import RegistryExplorer
from utils.admin import check_admin

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or secrets.token_hex(32)

# Same-origin only. The app is intentionally bound to localhost in run.py.
socketio = SocketIO(app, async_mode='threading')

DEMO_MODE = os.getenv('RCE_DEMO_MODE', '0').lower() in {'1', 'true', 'yes', 'on'}
DB_PATH = os.getenv('DB_PATH', 'registry.db')
explorer = RegistryExplorer(db_path=DB_PATH, demo_mode=DEMO_MODE)
register_handlers(socketio, explorer)


@app.route('/')
def index():
    return render_template('explorer.html', admin=check_admin(), demo_mode=DEMO_MODE)


@app.route('/api/browse/<path:path>')
def browse(path):
    try:
        return jsonify({
            'success': True,
            'path': path,
            'keys': explorer.get_subkeys(path),
            'values': explorer.get_values(path),
        })
    except Exception as exc:
        return jsonify({'success': False, 'error': str(exc)}), 500


@app.route('/api/search')
def search():
    term = request.args.get('q', '').strip()
    if len(term) < 2:
        return jsonify({'success': False, 'error': 'Search term must be at least 2 characters'}), 400
    try:
        return jsonify({'success': True, 'results': explorer.search(term)})
    except Exception as exc:
        return jsonify({'success': False, 'error': str(exc)}), 500


@app.route('/api/status')
@app.route('/api/sync-status')
def status():
    return jsonify(explorer.get_stats())


@app.route('/api/hives')
def hives():
    return jsonify([
        {'path': 'HKEY_CLASSES_ROOT', 'name': 'HKEY_CLASSES_ROOT'},
        {'path': 'HKEY_CURRENT_USER', 'name': 'HKEY_CURRENT_USER'},
        {'path': 'HKEY_LOCAL_MACHINE', 'name': 'HKEY_LOCAL_MACHINE'},
        {'path': 'HKEY_USERS', 'name': 'HKEY_USERS'},
        {'path': 'HKEY_CURRENT_CONFIG', 'name': 'HKEY_CURRENT_CONFIG'},
    ])
