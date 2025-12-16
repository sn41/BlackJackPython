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
)