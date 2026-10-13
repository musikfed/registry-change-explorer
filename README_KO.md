# Registry Change Explorer

Registry Change Explorer는 Windows Registry를 읽기 전용으로 탐색하는 독립 프로토타입입니다. 현재 MVP는 로컬 SQLite 인덱스를 만들고 빠른 웹 탐색/검색을 제공하며, 향후에는 변경 전/후 스냅샷의 읽기 쉬운 diff를 목표로 합니다.

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
