# Feedback Hub suggestion — English

## Title

Registry Change Explorer for Windows admins — snapshot, search and compare Registry changes

## Suggestion

Windows administrators have good tools for inspecting or editing a known Registry location, but it is harder to understand what exactly changed after installing software, updating a driver, applying a policy, or changing system configuration.

I would like to suggest a **Registry Change Explorer** workflow for administrators and developers.

Core scenario:

1. Create Registry Snapshot A.
2. Perform a controlled installation or configuration change.
3. Create Snapshot B.
4. Show a clear diff of added, removed, and modified keys/values.
5. Show before/after value data.
6. Filter by hive, path, value type, or change type.
7. Export the change set as a diagnostic report.
8. Keep the experience read-only by default.

I built an independent proof of concept that already demonstrates indexed Registry navigation and search, with safe synthetic demo data and a bilingual EN/RU UI.

Prototype and screenshots: https://github.com/musikfed/registry-change-explorer

The goal is not to make automatic destructive decisions. The goal is to give administrators a transparent way to understand Registry changes.
