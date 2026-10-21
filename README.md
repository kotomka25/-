# README.md

```markdown
# Лабораторная работа №1 — Определение ОС и сбор её параметров

Кроссплатформенный скрипт на Python, который определяет текущую операционную
систему (Linux / macOS / Windows), собирает её параметры и сохраняет результат
в файл формата JSON.

## Запуск

```bash
python my_script.py
```

В консоль выводится только название текущей ОС, например:

```
Текущая ОС: Linux
```

Все собранные параметры записываются в файл `os_info.json` в текущей рабочей
директории.

## Как определяется ОС

Используется стандартный модуль `platform`:

- `platform.system()` возвращает `Linux`, `Darwin` (macOS) или `Windows`;
- значение приводится к читаемому виду: `Linux` / `macOS` / `Windows`.

Скрипт не вызывает системные утилиты (`uname`, `sw_vers`, `systeminfo` и т.п.) —
вся информация получается средствами самого Python.

## Собираемые параметры

### Операционная система (`os`)

| Параметр | Описание | Источник |
|---|---|---|
| `system` | Системное имя ОС (`Linux`, `Darwin`, `Windows`) | `platform.system()` |
| `friendly_name` | Читаемое имя (`Linux`, `macOS`, `Windows`) | функция `detect_os()` |
| `release` | Версия ядра / ОС | `platform.release()` |
| `version` | Детальная версия сборки | `platform.version()` |
| `machine` | Архитектура (`x86_64`, `arm64`, `AMD64` и т.д.) | `platform.machine()` |
| `is_64bit` | Разрядность (`True`/`False`) | `sys.maxsize > 2**32` |
| `hostname` | Имя хоста | `platform.node()` |
| `platform_tag` | Значение `sys.platform` (`linux`, `darwin`, `win32`) | `sys.platform` |

### Среда исполнения Python (`python`)

| Параметр | Описание | Источник |
|---|---|---|
| `version` | Версия интерпретатора | `platform.python_version()` |
| `implementation` | Реализация (CPython, PyPy и др.) | `platform.python_implementation()` |
| `compiler` | Компилятор, которым собран Python | `platform.python_compiler()` |
| `executable` | Путь к интерпретатору | `sys.executable` |
| `encoding_default` | Кодировка по умолчанию | `sys.getdefaultencoding()` |

### Текущий процесс (`process`)

| Параметр | Описание | Источник |
|---|---|---|
| `pid` | Идентификатор процесса | `os.getpid()` |
| `user` | Имя пользователя | `getpass.getuser()` |
| `cwd` | Текущая рабочая директория | `os.getcwd()` |

### Мета-информация

| Параметр | Описание | Источник |
|---|---|---|
| `collected_at` | Время сбора параметров (ISO 8601) | `datetime.now()` |

## Структура JSON-файла

```json
{
  "collected_at": "2026-10-21T14:35:12",
  "os": {
    "system": "Linux",
    "friendly_name": "Linux",
    "release": "6.8.0-45-generic",
    "version": "#45-Ubuntu SMP PREEMPT_DYNAMIC",
    "machine": "x86_64",
    "is_64bit": true,
    "hostname": "ubuntu-vm",
    "platform_tag": "linux"
  },
  "python": {
    "version": "3.12.3",
    "implementation": "CPython",
    "compiler": "GCC 13.2.0",
    "executable": "/usr/bin/python3",
    "encoding_default": "utf-8"
  },
  "process": {
    "pid": 12345,
    "user": "student",
    "cwd": "/home/student/lab1"
  }
}
```

## Зависимости

Используется **только стандартная библиотека Python 3.6+**:

- `platform` — идентификация ОС и среды Python;
- `sys` — разрядность, путь к интерпретатору, `sys.platform`;
- `os` — PID и текущая директория;
- `getpass` — имя пользователя;
- `json` — запись результата;
- `datetime` — время сбора.

Внешние модули не используются: стандартных модулей достаточно для
поставленной задачи, а привлечение сторонних библиотек (например, `psutil`)
дало бы избыточные данные и усложнило запуск.

## Проверка кроссплатформенности

Скрипт корректно работает в Linux, macOS и Windows, поскольку:

- `platform.system()` возвращает корректное значение на всех трёх ОС;
- разрядность определяется через `sys.maxsize`, а не через
  `platform.architecture()` (последняя на Unix вызывает системную утилиту `file`);
- не используются вызовы внешних утилит ОС.

## Выполнила 

Студент: Котомина Мария Григорьвена
Группа: 5131001/60602
Дата сдачи: 2 октября 2026 г.
