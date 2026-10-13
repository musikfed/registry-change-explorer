# Registry Change Explorer

Registry Change Explorer 是独立的只读 Windows 注册表探索原型。当前 MVP 构建本地 SQLite 索引并提供快速 Web 导航与搜索，后续目标是实现变更前/后的快照与可读差异比较。

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
