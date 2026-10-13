# Registry Change Explorer

Registry Change Explorer нь Windows Registry-г зөвхөн унших бие даасан prototype. Одоогийн MVP локал SQLite индекс үүсгэж хурдан web navigation/search өгнө; дараагийн зорилго нь before/after snapshot diff юм.

## Architecture / Архитектура

```text
Windows Registry -> read-only indexer -> local SQLite index -> localhost web API/UI -> fast search and navigation -> future snapshot/diff workflow
```

## Project structure / Структура проекта

- local indexer — reads Registry keys/values without modifying them
- SQLite — local searchable index
- web UI — dual-pane navigation and search
- `docs/` — screenshots, publishing and outreach documentation

## Contact / Контакты

- Email: feudor.lab@yandex.ru
- Telegram: @Feudorlab1
