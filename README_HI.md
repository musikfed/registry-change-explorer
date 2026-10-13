# Registry Change Explorer

Registry Change Explorer Windows Registry का स्वतंत्र read-only प्रोटोटाइप है। वर्तमान MVP स्थानीय SQLite इंडेक्स बनाता है और तेज़ वेब नेविगेशन/खोज देता है; आगे का लक्ष्य before/after snapshots का मानव-पठनीय diff है।

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
