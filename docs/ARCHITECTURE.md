# Architecture / Архитектура

```text
Windows Registry -> read-only indexer -> local SQLite index -> localhost web API/UI -> fast search and navigation -> future snapshot/diff workflow
```

- local indexer — reads Registry keys/values without modifying them
- SQLite — local searchable index
- web UI — dual-pane navigation and search
- `docs/` — screenshots, publishing and outreach documentation
