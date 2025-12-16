Для того чтобы ваш проект правильно установился как пакет, файл `setup.py` должен находиться на уровень выше, чем папка
с кодом Game21.

С учетом того, что у вас есть файл `__init__.py`, ваша папка `Game21` является пакетом.

### 1. Правильная структура папок

Чтобы все сработало, ваша структура файлов должна выглядеть так:

```Plaintext

BlackJackPython/            <-- Корневая папка (создайте её)
├── setup.py                <-- Файл, который мы создаем сейчас
└── Game21/        <-- Ваша текущая папка с кодом
    ├── __init__.py
    ├── main.py
    ├── Deck.py
    └── Card.py
```

### 2. Содержимое setup.py

Создайте файл `setup.py` в корневой папке (BlackJackPython) со следующим содержимым:

```Python

from setuptools import setup, find_packages

setup(
    name='game21',  # Имя пакета для установки (pip install game21)
    version='1.0.0',  # Версия
    packages=find_packages(),  # Находит папку BlackJackPython автоматически
    install_requires=[  # В вашем коде нет внешних библиотек (только стандартные),
        # поэтому список пуст.
    ],
    entry_points={
        'console_scripts': [
            # Создает команду 'blackjack' в терминале, которая запускает функцию game из main.py
            'blackjack=Game21.main:game',
        ],
    },
    author='Your Name',
    description='A simple Blackjack game in Python',
)
```

### 3. Важное исправление в коде (main.py)

Поскольку теперь вы запускаете код как пакет, Python изменит то, как он ищет файлы Deck и Card. Старые импорты (from
Deck import Deck) перестанут работать, так как эти файлы больше не находятся в "корне" поиска, они находятся внутри
пакета Game21.

Вам нужно изменить начало файла Game21/main.py, добавив точку перед именами модулей (относительный импорт):

Было:

```Python
from Deck import Deck
from Card import Card
```

Стало (нужно заменить):

```Python
# Точка означает "искать в этой же папке пакета"
from .Deck import Deck
from .Card import Card
```

### Как запустить теперь?

1. Откройте терминал в папке `BlackJackPython` (где лежит setup.py).

2. Создайте и активируйте uv окружение (как обсуждали выше):

```bash
uv venv
# (активация: source .venv/bin/activate или .venv\Scripts\activate)
```

3. Установите проект:

```bash
uv pip install -e .
```

4. Запустите игру просто набрав команду:

```bash
game21
```

### Ошибки

pyproject.toml

```
[project]
name = "blackjackpython"
version = "0.1.0"
description = "Add your description here"
requires-python = ">=3.14"
dependencies = [
    "setuptools>=80.9.0",
]

```

setup.py

```
from setuptools import setup, find_packages

setup(
    name='game21',                 # Имя пакета для установки (pip install game-21)
    version='0.1.0',                # Версия
    packages=find_packages(),       # Находит папку Game21 автоматически

    install_requires=[              # В вашем коде нет внешних библиотек (только стандартные),
                                    # поэтому список пуст.
    ],

    entry_points = {
        'console_scripts': [
            # Создает команду 'game21' в терминале, которая запускает функцию game из main.py
            'game21=Game21.main:game',
        ],
    },

    author='ПО-2023-3',
    description='Практическая работа',
    url='https://github.com/sn41/BlackJackPython',
)`

```

> Обратите внимание на строку в вашем логе: ~ blackjackpython==0.1.0 (from file:///...)  
> А в вашем setup.py написано: name='game21'

> Что происходит: В вашей папке лежит файл pyproject.toml. Современные инструменты (и uv, и pip) считают этот файл "
> главным".  
> Если он существует, они читают настройки из него, а ваш setup.py (и прописанные в нем скрипты game21) игнорируется или
> перекрывается.  
> В вашем текущем pyproject.toml, скорее всего, нет секции, которая создает команду game21.



У вас есть два пути решения. Выберите один из них.

### Решение 1: Быстрое (Удалить конкурента)

Если вы хотите использовать именно тот код setup.py, который вы написали выше:

Удалите файл pyproject.toml из папки проекта.

```Bash
rm pyproject.toml
```

Переустановите проект:

```Bash
uv pip install --reinstall -e .
```

Теперь uv прочитает setup.py, увидит инструкцию console_scripts и создаст файл game21.

### Решение 2: Современное (Настроить pyproject.toml)

Если вы хотите делать "по-современному" (используя uv), лучше отказаться от setup.py и прописать всё в pyproject.toml.

- Удалите файл setup.py.

- Откройте файл pyproject.toml и полностью замените его содержимое на следующее:

```Ini, TOML

[project]
name = "game21"
version = "0.1.0"
description = "Практическая работа"
authors = [{name = "ПО-2023-3"}]
dependencies = []

# Вот эта секция создает команду запуска!
[project.scripts]
game21 = "Game21.main:game"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

Переустановите проект:

```Bash

uv pip install --reinstall -e .
```

# Нужно добавить ТОЧКУ перед Deck и Card

from .Deck import Deck
from .Card import Card
После этого команда game21 должна заработать

### Зачем [build-system]
requires = ["hatchling"]build-backend = "hatchling.build"

Это вопрос, касается самой "кухни" современной упаковки Python-проектов.

Если коротко: pyproject.toml — это просто текстовый файл с настройками (чертеж), он сам ничего не умеет делать. Ему нужен "подрядчик", который прочитает этот чертеж и фактически соберет проект.

Секция [build-system] говорит инструменту установки (например, uv или pip): "Эй, чтобы установить этот проект, тебе сначала нужно скачать вот этот инструмент (hatchling) и поручить ему сборку".

Разбор по строкам
```Ini, TOML

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

`requires = ["hatchling"]`

Что это: Список пакетов, которые нужно установить до того, как начнется установка вашего проекта.

Зачем: Ваш компьютер может вообще не знать, как собирать проекты. Эта строка говорит uv или pip: "Сначала скачай hatchling, он нам понадобится через секунду".

`build-backend = "hatchling.build"`

Что это: Точный адрес (путь к функции) внутри скачанного пакета, который выполнит работу.

Зачем: Инструмент установки (uv) спрашивает: "Окей, я скачал hatchling, к кому мне там обращаться?". Эта строка отвечает: "Обращайся к модулю hatchling.build, он знает, что делать".

#### Аналогия со стройкой

Представьте, что вы хотите построить дом (установить ваш проект).

`pyproject.toml` — это Чертеж. В нем написано: "Дом, 2 этажа, красная крыша" (имя проекта, версия, зависимости). Но чертеж не может сам построить дом.

`uv` (или `pip`) — это Заказчик. Он хочет получить готовый дом, но сам класть кирпичи не умеет.

`[build-system]` — это Контактная информация Подрядчика на первой странице чертежа.

`requires = ["hatchling"]`: "Нам нужна бригада строителей из компании 'Hatchling'".

`build-backend`: "Звонить прорабу по номеру 'hatchling.build'".

Если вы не укажете эту секцию, Заказчик (uv) посмотрит на чертеж и скажет: "Красиво, но кто это будет строить? Я не знаю".

#### Почему именно hatchling?
Раньше стандартом был `setuptools` (и файлы `setup.py`), но он был старым и громоздким. Сейчас в Python произошла революция стандартов (PEP 517), и появилось много "сборщиков" (backends). Вы можете выбрать любого:

- `Hatchling` (современный, быстрый, стандартный для многих новых инструментов).

- `Setuptools` (классика, если вы используете setup.py).

- `Poetry-core` (если вы используете Poetry).

- `Flit-core` (очень простой, для маленьких проектов).

`Hatchling` отлично работает с чистым `pyproject.toml` и не требует создания лишних файлов.

#### Можно ли использовать старый добрый setuptools?
Да! Если вы хотите использовать pyproject.toml, но остаться на "старых рельсах", секция будет выглядеть так:

```Ini, TOML
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

### Ошибки имен 

 hatchling (сборщик) пытается быть умным.

Он смотрит на имя проекта в pyproject.toml — name = "game21". Затем он ищет папку с таким же названием (обычно в нижнем регистре). Но ваша папка называется Game21 (с большой буквы).

Hatchling не смог автоматически сопоставить имя пакета с папкой и выдал ошибку: "Unable to determine which files to ship... The most likely cause of this is that there is no directory that matches the name of your project".

Вам нужно явно указать, в какой папке лежит ваш код.

Решение
Откройте файл pyproject.toml и добавьте в конец следующий блок:

```Ini, TOML

[tool.hatch.build.targets.wheel]
packages = ["Game21"]
Полный текст вашего pyproject.toml должен выглядеть так:
Ini, TOML

[project]
name = "game21"
version = "0.1.0"
description = "Практическая работа"
authors = [{name = "ПО-2023-3"}]
dependencies = []

[project.scripts]
game21 = "Game21.main:game"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

# --- ДОБАВЛЕНО ---
[tool.hatch.build.targets.wheel]
packages = ["Game21"]
```
