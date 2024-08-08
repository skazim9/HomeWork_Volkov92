# Проект "Виджет банковских операций клиента"

## Описание:

Этот проект нужен для обработки информации или банковских операций клиента.

## Project dependencies:

- The program uses the version Python 3.12.4
- flake8 = "7.1.0"
- black = "24.4.2"
- isort = "5.13.2"
- mypy = "1.10.0"

## Тесты: Содержит тесты функционала

---------- coverage: platform win32, python 3.12.4-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\decorators.py             21      2    90%
src\external_api.py           29      9    69%
src\generators.py             12      0   100%
src\masks.py                   7      1    86%
src\processing.py              7      0   100%
src\utils.py                  29     18    38%
src\widget.py                  7      0   100%
tests\__init__.py              0      0   100%
tests\conftest.py             12      0   100%
tests\test_decorators.py      44     14    68%
tests\test_func.py            17      0   100%
tests\test_generators.py      20      0   100%
tests\test_processing.py       7      0   100%
tests\test_utils.py           32      4    88%
----------------------------------------------
TOTAL                        244     48    80%


## Функции, которые мы будем использовать в этой версии кода:

- Функция скрывающая номер карты и счета
- Функция сортировки по дате
- Функция фильтрации в операциях по счетам
- Функция которая принимает список словарей с банковскими операциями и возвращает ID операции, в которых указана
заданная валюта
- Функция с описанием каждой операции
- Функция которая генерирует номера банковских карт
- Декоратор для логирования вызова функции и записи ее результата в файл или на консоль.
- функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
- функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
- функции get_data_from_csv и get_data_from_excel, которые позволяют считывать данные о финансовых операциях из файлов csv и excel.
- функция main, которая отвечает за основную логику проекта и связывает функциональности между собой. В модуле реализован пользовательский интерфейс по получению транзакций, а также их фильтрации.

## Структура проекта

По завершении этого проекта будет добавлен pytest, для запуска тестов и новый функционал

# Инструкция по установке

Чтобы скачать репозиторий:

`git clone https://github.com/skazim9/HomeWork_Volkov92.git`

Затем вам необходимо установить основные зависимости для запуска проекта в вашей системе:

```pip install -r requirements.txt```

## Команда проекта:

`Волков Максим`

## Контакт для связи с командой разработки:

`volkovmm07@gmail.com`

## Источники

Программа создана при поддержке онлайн-школы [skypro@skyeng.ru](https://sky.pro/#giftpopup)