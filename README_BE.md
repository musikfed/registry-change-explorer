# Registry Change Explorer

Registry Change Explorer — незалежны read-only прататып для даследавання Windows Registry. Бягучы MVP будуе лакальны SQLite-індэкс і дае хуткі вэб-пошук/навігацыю; далейшая мэта — зразумелы diff здымкаў «да/пасля».

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
