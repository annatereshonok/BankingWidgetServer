import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
HEADERS = {"apikey": API_KEY}
EXCHANGE_RATE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def currency_converter(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта — USD или EUR к рублю (RUB) через Exchange Rates Data API.

    Параметры:
        transaction: Словарь с данными о транзакции.
    Возвращает:
        Сумма транзакции в рублях.

    Исключения:
        ValueError: Если тип подаваемых данных не словарь.
        ValueError: Если нет ключей "operationAmount", "currency", "code" или "amount".
        ValueError: Если API не вернул успешный статус.
        requests.RequestException: Если произошла ошибка сети.
    """

    if not isinstance(transaction, dict):
        raise ValueError("Транзакция должна быть словарем.")

    try:
        currency_code = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])
    except KeyError:
        raise ValueError("Ошибка в структуре данных: отсутствуют нужные ключи.")

    if currency_code in ["USD", "EUR"]:
        payload = {"amount": str(amount), "from": currency_code, "to": "RUB"}

        try:
            response = requests.get(EXCHANGE_RATE_URL, headers=HEADERS, params=payload)
            response.raise_for_status()
        except requests.RequestException:
            raise requests.RequestException("Ошибка при запросе к API")

        try:
            amount_converted = response.json()["result"]
        except KeyError:
            raise ValueError(f"Ошибка в данных API: нет ключа 'result' для {currency_code}")

        return float(amount_converted)

    return float(amount)
