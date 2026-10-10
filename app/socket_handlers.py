"""Socket.IO events for registry synchronization."""

import time
from flask import request
from flask_socketio import emit


def register_handlers(socketio, explorer):
    @socketio.on('connect')
    def handle_connect():
        emit('connected', {
            'message': 'Connected to Registry Change Explorer',
            'time': time.time(),
        })
        emit('status_update', explorer.get_stats())

    @socketio.on('request_sync')
    def handle_sync_request(_data=None):
        client_id = request.sid
        if not explorer.start_sync():
            emit('sync_error', {'message': 'Синхронизация уже выполняется'})
            return

        emit('sync_start', {'message': 'Синхронизация запущена'})

        def watch_sync():
            last_progress = -1
            while explorer.is_syncing:
                current = explorer.sync_progress
                if current != last_progress:
                    socketio.emit('sync_progress', {'current': current}, to=client_id)
                    last_progress = current
                socketio.sleep(0.25)

            stats = explorer.get_stats()
            if stats.get('error'):
                socketio.emit('sync_error', {'message': stats['error']}, to=client_id)
            else:
                socketio.emit('sync_complete', {'stats': stats}, to=client_id)

        socketio.start_background_task(watch_sync)

    @socketio.on('ping')
    def handle_ping(data):
        emit('pong', {'time': time.time(), 'echo': data})

    return socketio
