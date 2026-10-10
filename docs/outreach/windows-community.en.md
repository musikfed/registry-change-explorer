# Windows community post — English

## Suggested title

**I built a read-only Registry Explorer prototype — would a Snapshot A/B diff be useful to Windows admins?**

## Post

I have been experimenting with a Windows admin/developer tool called **Registry Change Explorer**.

The current prototype is intentionally read-only: it indexes Registry keys/values into local SQLite, then provides fast navigation and search in a dual-pane UI. It also has a synthetic demo mode so the repository and screenshots do not expose a real machine's Registry data.

The feature I am most interested in is the next one:

**Snapshot A → install/change something → Snapshot B → show exactly what changed.**

The diff would focus on:

- added / removed / modified keys;
- added / removed / modified values;
- before/after value data;
- filters by hive/path/change type;
- exportable diagnostic reports.

I am deliberately not positioning it as an automatic Registry modification tool. The interesting problem is **explainability**: helping an admin understand what an installer, policy, driver, or configuration change actually did.

The prototype has English and Russian UI/screenshots and a public roadmap.

**GitHub:** https://github.com/musikfed/registry-change-explorer

For people who administer or troubleshoot Windows: would a before/after Registry diff be useful in real work? What would it need to show before you would trust it?
