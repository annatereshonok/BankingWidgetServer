from unittest.mock import patch

import pytest
import requests

from src.external_api import currency_converter


@patch("src.external_api.requests.get")
def test_currency_converter_success_usd(mocked_get, transaction_currency_converter_usd):

    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"result": 1000.0}
    expected_result = 1000.0

    assert currency_converter(transaction_currency_converter_usd) == expected_result
    mocked_get.assert_called_once()


def test_currency_converter_success_rub(transaction_currency_converter_rub):
    assert currency_converter(transaction_currency_converter_rub) == 100.0


@patch("src.external_api.requests.get", side_effect=requests.exceptions.HTTPError())
def test_currency_converter_failed_request(mocked_get, transaction_currency_converter_usd):
    with pytest.raises(requests.exceptions.RequestException, match="Ошибка при запросе к API"):
        currency_converter(transaction_currency_converter_usd)


@patch("src.external_api.requests.get")
def test_currency_converter_no_result(mocked_get, transaction_currency_converter_usd):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {}

    with pytest.raises(ValueError, match="Ошибка в данных API: нет ключа 'result' для USD"):
        currency_converter(transaction_currency_converter_usd)


def test_currency_converter_keyerror(transaction_currency_converter_keys):
    transaction, expected_error = transaction_currency_converter_keys
    with pytest.raises(ValueError, match=expected_error):
        currency_converter(transaction)
