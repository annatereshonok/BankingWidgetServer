import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_positive(transactions_example):
    generator_result = filter_by_currency(transactions_example, "USD")
    assert next(generator_result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator_result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_negative(params_filter_by_currency_negative):
    transactions, currency, expected_exception_message = params_filter_by_currency_negative
    print(transactions)
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency(transactions, currency)
    assert str(exc_info.value) == expected_exception_message


def test_transaction_descriptions_positive(transactions_example):
    generator_result = transaction_descriptions(transactions_example)
    assert next(generator_result) == "Перевод организации"
    assert next(generator_result) == "Перевод со счета на счет"
    assert next(generator_result) == "Перевод со счета на счет"
    assert next(generator_result) == "Перевод с карты на карту"


def test_transaction_descriptions_negative(params_transaction_descriptions_negative):
    transactions, expected_exception_message = params_transaction_descriptions_negative
    with pytest.raises(ValueError) as exc_info:
        transaction_descriptions(transactions)
    assert str(exc_info.value) == expected_exception_message


def test_card_number_generator_positive():
    generator_result = card_number_generator(1, 5)
    assert next(generator_result) == "0000 0000 0000 0001"
    assert next(generator_result) == "0000 0000 0000 0002"
    assert next(generator_result) == "0000 0000 0000 0003"
    assert next(generator_result) == "0000 0000 0000 0004"
    assert next(generator_result) == "0000 0000 0000 0005"


def test_card_number_generator_negative(params_card_number_generator_negative):
    start, end, expected_exception_message = params_card_number_generator_negative
    with pytest.raises(ValueError) as exc_info:
        card_number_generator(start, end)
    assert str(exc_info.value) == expected_exception_message
