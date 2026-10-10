# GitHub publishing checklist

## Suggested repository name

`registry-change-explorer`

## Suggested description

> Read-only Windows Registry explorer with a fast SQLite index and a roadmap toward snapshot/diff analysis for administrators and developers.

## Suggested topics

`windows` · `registry` · `sysadmin` · `windows-admin` · `python` · `sqlite` · `flask` · `diagnostics` · `developer-tools` · `forensics`

## Before making the repository public

- Confirm there is no `registry.db`, `.env`, SQLite journal, real-machine export, token, or private archive in the working tree.
- Keep screenshots based on demo/synthetic data only.
- Decide on a software license deliberately. No license is included in this package.
- Add the repository URL to the outreach drafts after the repo exists.
- Create an initial release such as `v0.1.0-prototype` only after a clean Windows demo run.

## Suggested first commit message

```text
feat: publish Registry Change Explorer prototype
```

## Suggested first release title

```text
Registry Change Explorer v0.1 — read-only public prototype
```

## Suggested release summary

Registry Change Explorer v0.1 is a read-only prototype for fast Windows Registry browsing and search. It builds a local SQLite index, provides a bilingual EN/RU interface, and includes a safe synthetic demo mode. The next major milestone is Registry snapshot comparison: capture before/after states and explain exactly what changed.
