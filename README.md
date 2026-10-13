# Registry Change Explorer

> **English** · [Русский](README.ru.md)

📖 **Project article / Статья:** [ARTICLE.md](ARTICLE.md)

**Registry Change Explorer** is an independent, read-only prototype for fast Windows Registry navigation and search, with a longer-term goal: make Registry changes understandable to administrators, developers, support engineers, and security-minded power users.

The current MVP builds a local SQLite index of Registry keys and values and provides a fast dual-pane web UI. The project roadmap extends that foundation toward **Snapshot A → system change → Snapshot B → human-readable diff**.

> Independent community project. Not affiliated with or endorsed by Microsoft.

## Screenshots

### English UI

![Registry Change Explorer — English main view](docs/screenshots/en/main.png)

![Registry Change Explorer — English search](docs/screenshots/en/search.png)

### Русский интерфейс

![Registry Change Explorer — русский основной экран](docs/screenshots/ru/main.png)

![Registry Change Explorer — русский поиск](docs/screenshots/ru/search.png)

The UI includes an **EN / RU** language switch.

## Why this project exists

Windows has excellent low-level Registry tooling, but answering a practical question can still take too much manual work:

**“What exactly changed in the Registry after I installed this application, updated a driver, applied a policy, or changed a system setting?”**

Registry Change Explorer is an experiment around a safer workflow:

1. Inspect and search an indexed Registry quickly.
2. Capture a baseline snapshot.
3. Perform a controlled system change.
4. Capture a second snapshot.
5. Compare added, removed, and modified keys/values.
6. Export or review the change set before taking any action.

Only step 1 is implemented in the current MVP. Snapshot/diff is the primary next product direction.

## Current MVP

- read-only Registry browsing;
- local SQLite index of keys and values;
- fast search across paths, key names, value names, and value data;
- dual-pane navigation plus Registry tree;
- background index refresh with progress status;
- localhost-only web UI;
- English and Russian UI;
- safe demo mode with synthetic Registry data;
- repository rules that keep `registry.db`, `.env`, journals, and local archives out of Git.

## Quick start on Windows

Requirements: **Windows 10/11** and **Python 3.10+**.

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python run.py
```

Then open:

```text
http://127.0.0.1:5000
```

You can also use `run.bat`.

### Demo mode

Demo mode does **not** read the real Windows Registry. It loads a small synthetic dataset for UI evaluation, screenshots, and development.

```powershell
$env:RCE_DEMO_MODE = "1"
python run.py
```

Or run `run_demo.bat`.

## Keyboard controls

| Key | Action |
| --- | --- |
| `F3` | Focus search |
| `F5` | Refresh active panel |
| `F9` | Refresh local index |
| `Tab` | Switch active panel |

## Architecture

```text
app/                 Flask + Socket.IO HTTP/events layer
core/                Registry traversal and index orchestration
core/demo_data.py    synthetic safe demo dataset
database/            SQLite schema and connection manager
templates/           bilingual web UI
docs/                screenshots, articles, outreach drafts
tests/               demo-mode smoke tests
```

Data flow:

```text
Windows Registry -> RegistryLowLevel -> RegistryExplorer -> SQLite -> Flask API -> Web UI
```

## Configuration

Copy `.env.example` to `.env` if you want to override defaults:

```env
DB_PATH=registry.db
RCE_DEMO_MODE=0
FLASK_DEBUG=0
PORT=5000
```

`registry.db` may contain paths and values from a specific machine. It is intentionally excluded from Git and should not be attached to issues or releases without reviewing its contents first.

## Product direction

The highest-value next step is not destructive automation. It is **explainability**.

Planned direction:

1. SQLite FTS for large Registry indexes.
2. Snapshot storage with metadata and timestamps.
3. Snapshot diff: added / removed / modified keys and values.
4. Filters by hive, path, value type, and change type.
5. Export to JSON / CSV / `.reg`-friendly reports.
6. Bookmarks and history.
7. Optional attribution experiments that help correlate changes with an installer/process when technically reliable.
8. Guarded write operations only after backup, preview, explicit confirmation, and recovery design are mature.

See [ROADMAP.md](ROADMAP.md).

## Articles

- [English: Why Windows admins need a Registry Change Explorer](docs/articles/registry-change-explorer.en.md)
- [Русский: Зачем администраторам Windows нужен Registry Change Explorer](docs/articles/registry-change-explorer.ru.md)

## Community / Microsoft outreach drafts

- [Microsoft / Windows platform pitch — English](docs/outreach/microsoft-email.en.md)
- [Письмо / питч — русский вариант](docs/outreach/microsoft-email.ru.md)
- [Windows community post — English](docs/outreach/windows-community.en.md)
- [Пост для Windows-сообщества — русский](docs/outreach/windows-community.ru.md)
- [Feedback Hub suggestion — English](docs/outreach/feedback-hub.en.md)
- [Feedback Hub suggestion — Русский](docs/outreach/feedback-hub.ru.md)

## Security and privacy

See [SECURITY.md](SECURITY.md). Real Registry indexes may contain machine-specific information; the committed screenshots use synthetic demo data.

## Testing

The demo smoke test does not require access to a real Windows Registry:

```bash
python -m unittest discover -s tests -v
```

A GitHub Actions workflow is included at `.github/workflows/ci.yml`.

## Public-repository note

A software license is intentionally **not selected in this package**. Decide on the licensing strategy before public release, especially if you want to keep commercial options open. See [docs/GITHUB_PUBLISHING.md](docs/GITHUB_PUBLISHING.md).

## Contact / Контакты

- Email: [feudor.lab@yandex.ru](mailto:feudor.lab@yandex.ru)
- Telegram: [@Feudorlab1](https://t.me/Feudorlab1)

## Languages / Языки

[English](README_EN.md) · [Русский](README_RU.md) · [हिन्दी](README_HI.md) · [简体中文](README_ZH-CN.md) · [Қазақша](README_KK.md) · [Монгол](README_MN.md) · [Саха тыла](README_SAH.md) · [Беларуская](README_BE.md) · [한국어](README_KO.md)
