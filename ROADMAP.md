# Roadmap

Registry Change Explorer is intentionally developed from **inspection and explainability first** toward more advanced administrative workflows.

## 0.1 — Public prototype

- Read-only Registry browser
- SQLite-backed local index
- Search across keys and values
- English / Russian UI
- Demo mode
- GitHub CI and documentation

## 0.2 — Search at scale

- SQLite FTS
- Result ranking and highlighting
- Path/type filters
- Copy path/value actions
- Bookmarks and history

## 0.3 — Registry snapshots

- Named snapshots
- Timestamp + machine metadata
- Snapshot size/statistics
- Export and import of sanitized snapshots

## 0.4 — Change Explorer

- Snapshot A vs Snapshot B
- Added / removed / modified keys
- Added / removed / modified values
- Before/after value view
- Filter by hive/path/change type
- Export diff to JSON/CSV/report

## 0.5 — Admin workflow experiments

- Correlate a diff with a controlled installation or configuration session
- Optional event/process context where reliable
- Shareable diagnostic reports with privacy warnings

## Later — guarded write operations

Any write functionality should require a mature safety model: preview, backup, explicit confirmation, audit trail, and recovery. Read-only analysis remains the default.
