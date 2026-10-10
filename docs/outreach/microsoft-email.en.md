# Microsoft / Windows team outreach — English draft

**Suggested subject:** Prototype idea for Windows admins: Registry Change Explorer (snapshot + diff workflow)

Hello,

I am building an independent prototype called **Registry Change Explorer** around a simple Windows administration problem: it is easy to inspect a known Registry location, but much harder to answer **“what exactly changed?”** after an installation, driver update, policy change, or system configuration change.

The current prototype is read-only. It builds a local SQLite index of Windows Registry keys and values and provides fast navigation and search through a bilingual EN/RU interface.

The feature direction I would like to propose is a **Registry snapshot and comparison workflow**:

- create Snapshot A;
- perform a controlled installation/configuration change;
- create Snapshot B;
- show added, removed, and modified keys/values;
- display old/new value data;
- filter by hive/path/change type;
- export a diagnostic report;
- keep the workflow read-only by default.

I believe this could be useful to Windows administrators, desktop support, software developers, QA/packaging teams, and troubleshooting workflows. Conceptually it may fit the Windows admin ecosystem, a PowerToys-style experiment, or the diagnostic philosophy associated with Sysinternals.

I have prepared a working proof of concept with source code, safe synthetic demo data, English/Russian screenshots, and a technical roadmap.

**Repository:** https://github.com/musikfed/registry-change-explorer

I would appreciate feedback on whether this problem and workflow align with any current Windows administration or developer-tooling initiatives, and where the most appropriate channel would be to discuss the concept further.

Thank you for your time,

[YOUR NAME]
[GitHub profile / contact]

---

## Short version

**Subject:** Registry Change Explorer — Windows admin prototype

Hello,

I built a read-only Windows Registry exploration prototype and would like to propose a broader admin feature: **Snapshot A → system change → Snapshot B → clear Registry diff**.

The goal is to help admins and developers understand exactly which Registry keys/values were added, removed, or modified after software installation, driver/policy changes, or troubleshooting steps.

Prototype, screenshots and roadmap: https://github.com/musikfed/registry-change-explorer

If this is relevant to Windows admin tooling, PowerToys, or diagnostic tooling, I would be grateful for feedback or a pointer to the right team/channel.

Best regards,
[YOUR NAME]
