# Смирнов Артём Дмитриевич, группа 221

## Описание

Данный проект создан для того, чтобы научиться автоматизировать тестирование кода и развертывать базовый CI/CD.

## Статусы

![Test Status](https://github.com/KorolKrinzha/hse_tp_hw_2/actions/workflows/TestNumbersOperator.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## Технологический стек

- Python - ЯП
- unittest - Python-модуль для тестирования
- GitHub Actions - CI-система

## Основные файлы

- **NumbersOperator.py** - файл с классом NumbersOperator. Используется для работы с числами из файла
- **test_NumbersOperator.py** - тесты, проверяющие работу класса NumbersOperator на данных разных размеров. Также в файле присутствуют обработки ошибок
- **tests_txt** - папка с тестами в формате txt
- **timetests.py** - python-скрипт, который измеряет скорость выполнения функций при разных объемах данных и на основе результатов составляет график
- **TimeTests.ipynb** - дублирует timetests.py по коду, но результаты работы записаны в более удобном для восприятия формате
- **imgs** - папка с изображениями. Необходима для хранения результата работы timetests.py и для иллюстраций в MD-файлах
- **LICENSE.md** - лицензия MIT
