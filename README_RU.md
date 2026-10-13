# Registry Change Explorer

Registry Change Explorer — независимый read-only прототип для исследования реестра Windows. Текущий MVP строит локальный SQLite-индекс и даёт быстрый веб-поиск/навигацию; дальнейшая цель — сравнение снимков «до/после» с понятным diff.

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
