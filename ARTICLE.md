# Registry Change Explorer — article / статья

> **English below** · **Русская версия ниже**

## Русский

# Зачем администраторам Windows нужен Registry Change Explorer

Администратор Windows часто знает, **где искать**, но гораздо сложнее понять, **что именно изменилось**.

Установили программу, обновили драйвер, применили политику, изменили настройку оболочки или разбираетесь, почему система начала вести себя иначе — в Registry могут появиться десятки и тысячи изменений. `regedit` отлично подходит, когда известен конкретный путь. Но расследовательский вопрос обычно другой:

> Что изменилось между рабочим состоянием и состоянием после изменения системы?

Из этого вопроса и выросла идея **Registry Change Explorer**.

Проект не строится вокруг автоматического изменения Registry. Центральный сценарий безопаснее и полезнее для диагностики: **проиндексировать, посмотреть, сделать снимок, сравнить, объяснить**.

Желаемый workflow:

1. Создать **Снимок A** до контролируемого изменения.
2. Установить программу, обновить драйвер, применить политику или изменить настройку Windows.
3. Создать **Снимок B**.
4. Показать понятный diff: добавленные, удалённые и изменённые ключи и значения.
5. Отфильтровать изменения по hive, path, типу значения или типу изменения.
6. Экспортировать результат как диагностический отчёт.

Текущий публичный прототип специально начинается в read-only режиме. Он умеет обходить Registry, сохранять локальный SQLite-индекс и выполнять быстрый поиск без полного рекурсивного обхода при каждом запросе.

Главная следующая цель — настоящий **Snapshot A / Snapshot B diff** для администраторов, разработчиков, QA, support и troubleshooting.

Полная русская версия: [docs/articles/registry-change-explorer.ru.md](docs/articles/registry-change-explorer.ru.md)

---

## English

# Why Windows admins need a Registry Change Explorer

Windows administrators often know **where** to look, but the hard part is understanding **what changed**.

Install an application, update a driver, apply a policy, change a shell setting, or troubleshoot a machine and the Windows Registry can accumulate dozens or thousands of relevant changes. `regedit` is excellent for inspecting a known location. It is less convenient when the question is investigative:

> What changed between the working state and the broken state?

That question is the reason I started **Registry Change Explorer**.

The project is not built around automatic modification of the Registry. Its core idea is safer and more useful for diagnostics: **index, inspect, snapshot, compare, explain**.

The desired workflow:

1. Create **Snapshot A** before a controlled change.
2. Install software, update a driver, apply a policy, or change a Windows setting.
3. Create **Snapshot B**.
4. Show a focused diff of added, removed, and modified keys and values.
5. Filter the diff by hive, path, value type, or change type.
6. Export the result as a diagnostic report.

The current public prototype deliberately starts in read-only mode and provides local SQLite-backed Registry navigation and search.

The next major milestone is a real **Snapshot A / Snapshot B diff** for administrators, developers, QA, support, and troubleshooting.

Full English version: [docs/articles/registry-change-explorer.en.md](docs/articles/registry-change-explorer.en.md)
