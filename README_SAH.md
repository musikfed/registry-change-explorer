# Registry Change Explorer

Registry Change Explorer — Windows Registry-ны уларытан эрэ көрөр туспа prototype. Билигин MVP локальнай SQLite индекс оҥорон, түргэн web navigation/search биэрэр; салгыы before/after snapshot diff оҥоруу соруктаах.

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
