# Registry Change Explorer

> [English](README.md) · **Русский**

**Registry Change Explorer** — независимый read-only прототип для быстрой навигации и поиска по Windows Registry. Главная долгосрочная идея проекта — сделать изменения реестра понятными для системных администраторов, разработчиков, инженеров поддержки и продвинутых пользователей.

Текущий MVP создаёт локальный SQLite-индекс ключей и значений и даёт быстрый двухпанельный интерфейс. Следующий продуктовый шаг — сценарий **Снимок A → изменение системы → Снимок B → понятный diff**.

> Независимый community-проект. Не связан с Microsoft и не является официальным продуктом Microsoft.

## Скриншоты

### Русский интерфейс

![Registry Change Explorer — основной экран](docs/screenshots/ru/main.png)

![Registry Change Explorer — поиск](docs/screenshots/ru/search.png)

### English UI

![Registry Change Explorer — English main view](docs/screenshots/en/main.png)

![Registry Change Explorer — English search](docs/screenshots/en/search.png)

В интерфейсе есть переключатель **EN / RU**.

## Зачем нужен проект

В Windows есть сильные низкоуровневые инструменты для работы с Registry, но на практический вопрос всё ещё бывает сложно быстро ответить:

**«Что именно изменилось в реестре после установки программы, обновления драйвера, применения политики или изменения системной настройки?»**

Registry Change Explorer развивает более безопасный сценарий:

1. Быстро просмотреть и найти нужное в индексированном реестре.
2. Создать исходный снимок.
3. Выполнить контролируемое изменение системы.
4. Создать второй снимок.
5. Сравнить добавленные, удалённые и изменённые ключи/значения.
6. Изучить или экспортировать набор изменений до любых действий.

В текущем MVP реализован первый пункт. Snapshot/diff — главный следующий этап развития.

## Что уже есть

- read-only просмотр Windows Registry;
- локальный SQLite-индекс ключей и значений;
- быстрый поиск по пути, имени ключа, имени значения и данным;
- двухпанельная навигация и дерево Registry;
- фоновое обновление индекса со статусом прогресса;
- web UI только на `localhost`;
- русский и английский интерфейс;
- безопасный demo mode с синтетическими данными;
- защита репозитория от случайного коммита `registry.db`, `.env`, журналов SQLite и локальных архивов.

## Быстрый запуск на Windows

Требования: **Windows 10/11** и **Python 3.10+**.

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python run.py
```

После запуска откройте:

```text
http://127.0.0.1:5000
```

Также есть `run.bat`.

### Demo mode

Demo mode **не читает реальный реестр** и загружает небольшой синтетический набор данных для просмотра UI, разработки и скриншотов.

```powershell
$env:RCE_DEMO_MODE = "1"
python run.py
```

Или используйте `run_demo.bat`.

## Горячие клавиши

| Клавиша | Действие |
| --- | --- |
| `F3` | Перейти к поиску |
| `F5` | Обновить активную панель |
| `F9` | Обновить локальный индекс |
| `Tab` | Сменить активную панель |

## Архитектура

```text
app/                 Flask + Socket.IO HTTP/events
core/                обход Registry и управление индексом
core/demo_data.py    безопасные синтетические demo-данные
database/            SQLite schema / connection manager
templates/           двуязычный web UI
docs/                скриншоты, статьи и outreach-материалы
tests/               smoke-test demo mode
```

Поток данных:

```text
Windows Registry -> RegistryLowLevel -> RegistryExplorer -> SQLite -> Flask API -> Web UI
```

## Конфигурация

Скопируйте `.env.example` в `.env`, если нужно изменить значения по умолчанию:

```env
DB_PATH=registry.db
RCE_DEMO_MODE=0
FLASK_DEBUG=0
PORT=5000
```

`registry.db` может содержать пути и значения с конкретного компьютера. База намеренно исключена из Git. Не прикладывайте её к issue/release, пока не проверили содержимое.

## Куда развивать

Главная ценность проекта — не автоматические разрушительные действия, а **объяснимость изменений**.

Приоритеты:

1. SQLite FTS для больших индексов.
2. Хранение снимков с метаданными и временем.
3. Diff снимков: добавленные / удалённые / изменённые ключи и значения.
4. Фильтры по hive, path, типу значения и типу изменения.
5. Экспорт JSON / CSV / отчётов, совместимых с `.reg`-workflow.
6. Закладки и история.
7. Эксперименты по сопоставлению изменений с installer/process — только там, где результат можно показать достоверно.
8. Изменение Registry — только после зрелого backup/preview/confirmation/recovery workflow.

См. [ROADMAP.md](ROADMAP.md).

## Статьи

- [Русский: Зачем администраторам Windows нужен Registry Change Explorer](docs/articles/registry-change-explorer.ru.md)
- [English: Why Windows admins need a Registry Change Explorer](docs/articles/registry-change-explorer.en.md)

## Материалы для Windows/Microsoft community

- [Письмо / питч — русский вариант](docs/outreach/microsoft-email.ru.md)
- [Microsoft / Windows platform pitch — English](docs/outreach/microsoft-email.en.md)
- [Пост для Windows-сообщества — русский](docs/outreach/windows-community.ru.md)
- [Windows community post — English](docs/outreach/windows-community.en.md)
- [Feedback Hub suggestion — English](docs/outreach/feedback-hub.en.md)
- [Feedback Hub suggestion — Русский](docs/outreach/feedback-hub.ru.md)

## Безопасность и приватность

См. [SECURITY.md](SECURITY.md). Реальный индекс Registry может содержать данные конкретной машины; все скриншоты в репозитории используют синтетические demo-данные.

## Проверка

Demo smoke-test не требует доступа к реальному Windows Registry:

```bash
python -m unittest discover -s tests -v
```

Также в проекте есть GitHub Actions workflow: `.github/workflows/ci.yml`.

## Перед публичной публикацией

В пакет намеренно **не добавлена лицензия**. Перед публикацией стоит осознанно выбрать лицензионную стратегию, особенно если хочется сохранить коммерческие варианты развития. Подробнее: [docs/GITHUB_PUBLISHING.md](docs/GITHUB_PUBLISHING.md).
