# Security and privacy

Registry Change Explorer is designed as a **local, read-only prototype**. The web UI binds to `127.0.0.1` and the current MVP does not implement Registry write/delete operations.

## Sensitive local data

A real Registry index may contain machine-specific paths, product identifiers, usernames, application configuration, or other environment details. Treat `registry.db`, Registry exports, logs, and screenshots from a real machine as potentially sensitive.

The repository intentionally ignores local database files, `.env`, SQLite journals, archives, and common editor/runtime artifacts. The screenshots committed to this repository use synthetic demo data.

## Reporting a security issue

If you discover a security problem, avoid publishing machine-specific Registry data in a public issue. Share only the minimum sanitized reproduction needed to explain the problem.

Before future write functionality is considered production-ready, it should include explicit previews, backups, confirmation, auditability, and a tested recovery path.
