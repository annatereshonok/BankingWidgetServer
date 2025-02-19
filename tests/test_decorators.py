import re

import pytest

from src.generators import transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def check_log_output(capsys, expected_output):
    """Проверка, что лог в captured.out соответствует ожидаемому"""
    captured = capsys.readouterr()
    assert captured.out == expected_output


def check_log_in_file(filename, expected_output):
    """Проверка, что ожидаемый лог содержится в указанном файле"""
    with open(filename, "r", encoding="utf-8") as file:
        log_content = file.read()
    assert expected_output in log_content


def check_succesfull_log_console(func, *args, expected_output, capsys):
    """Тестирует успешное выполнение функции и логи в captured.out"""
    func(*args)
    check_log_output(capsys, expected_output)


def check_error_log(func, *args, exception_type):
    """Тестирует ошибку в выполнении функции и логи в captured.out"""
    with pytest.raises(exception_type):
        func(*args)


def test_log_decorator(capsys):
    # Тестирование get_mask_account
    account = "73654108430135874305"
    expected_output = (
        "[INFO] Запуск функции 'get_mask_account' с аргументами: ('73654108430135874305',), {}\n"
        "[INFO] Функция 'get_mask_account' выполнена успешно. Результат: **4305\n\n"
    )
    check_succesfull_log_console(get_mask_account, account, expected_output=expected_output, capsys=capsys)

    account = "700079228960636132"
    expected_output = (
        "[INFO] Запуск функции 'get_mask_account' с аргументами: ('700079228960636132',), {}\n"
        "[ERROR] Ошибка в функции 'get_mask_account': ValueError. Входные параметры: ('700079228960636132',), {}\n\n"
    )
    check_error_log(get_mask_account, account, exception_type=ValueError)
    check_log_output(capsys, expected_output)

    # Тестирование get_mask_card_number
    expected_output = (
        "[INFO] Запуск функции 'get_mask_card_number' с аргументами: ('7000792289606361',), {}\n"
        "[INFO] Функция 'get_mask_card_number' выполнена успешно. Результат: 7000 79** **** 6361\n"
    )
    get_mask_card_number("7000792289606361")
    check_log_in_file("log_masks.txt", expected_output)

    card_number = "1234-5678-9012-3456"
    expected_output = (
        "[INFO] Запуск функции 'get_mask_card_number' с аргументами: ('1234-5678-9012-3456',), {}\n"
        "[ERROR] Ошибка в функции 'get_mask_card_number': ValueError. "
        "Входные параметры: ('1234-5678-9012-3456',), {}\n"
    )
    check_error_log(get_mask_card_number, card_number, exception_type=ValueError)
    check_log_in_file("log_masks.txt", expected_output)

    # Тестирование mask_account_card
    card_number = "Maestro 1596837868705199"
    expected_output = (
        "[INFO] Запуск функции 'mask_account_card' с аргументами: ('Maestro 1596837868705199',), {}\n"
        "[INFO] Функция 'mask_account_card' выполнена успешно. Результат: Maestro 1596 83** **** 5199\n\n"
    )
    check_succesfull_log_console(mask_account_card, card_number, expected_output=expected_output, capsys=capsys)

    card_number = "Maestro 73654108430135874305"
    expected_output = (
        "[INFO] Запуск функции 'mask_account_card' с аргументами: ('Maestro 73654108430135874305',), {}\n"
        "[ERROR] Ошибка в функции 'mask_account_card': ValueError. "
        "Входные параметры: ('Maestro 73654108430135874305',), {}\n\n"
    )
    check_error_log(mask_account_card, card_number, exception_type=ValueError)
    check_log_output(capsys, expected_output)

    # Тестирование get_date
    expected_output = (
        "[INFO] Запуск функции 'get_date' с аргументами: ('2024-02-03T15:30:45.123456',), {}\n"
        "[INFO] Функция 'get_date' выполнена успешно. Результат: 03.02.2024\n\n"
    )
    get_date("2024-02-03T15:30:45.123456")
    check_log_in_file("log_widget.txt", expected_output)

    check_date = ""
    expected_output = (
        "[INFO] Запуск функции 'get_date' с аргументами: ('',), {}\n"
        "[ERROR] Ошибка в функции 'get_date': ValueError. Входные параметры: ('',), {}\n\n"
    )
    check_error_log(get_date, check_date, exception_type=ValueError)
    check_log_in_file("log_widget.txt", expected_output)

    # Тестирование sort_by_date
    state_args = (
        [
            {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        True,
    )
    expected_output = (
        "[INFO] Запуск функции 'sort_by_date' с аргументами: ("
        "[{'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, "
        "{'id': 2, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, "
        "{'id': 3, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, "
        "{'id': 4, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], True), {}\n"
        "[INFO] Функция 'sort_by_date' выполнена успешно. Результат: ["
        "{'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, "
        "{'id': 4, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, "
        "{'id': 3, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, "
        "{'id': 2, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]\n\n"
    )
    check_succesfull_log_console(sort_by_date, *state_args, expected_output=expected_output, capsys=capsys)

    # Тестирование filter_by_state
    transactions = 123
    expected_output = (
        "[INFO] Запуск функции 'filter_by_state' с аргументами: (123,), {}\n"
        "[ERROR] Ошибка в функции 'filter_by_state': ValueError. Входные параметры: (123,), {}\n\n"
    )
    check_error_log(filter_by_state, transactions, exception_type=ValueError)
    check_log_in_file("log_processing.txt", expected_output)

    # Тестирование transaction_descriptions
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    transaction_descriptions(transactions)
    expected_output = (
        f"[INFO] Запуск функции 'transaction_descriptions' с аргументами: ({transactions},), {{}}\n"
        f"[INFO] Функция 'transaction_descriptions' выполнена успешно. "
        f"Результат: <generator object transaction_descriptions.<locals>.<genexpr> at"
    )
    pattern = re.escape(expected_output) + r".*"
    captured = capsys.readouterr()
    assert re.match(pattern, captured.out)
