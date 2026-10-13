# Registry Change Explorer

Registry Change Explorer — Windows Registry-ді тек оқуға арналған тәуелсіз прототип. Қазіргі MVP жергілікті SQLite индексін құрып, жылдам веб-навигация/іздеу береді; келесі мақсат — «дейін/кейін» snapshot айырмасын түсінікті көрсету.

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
