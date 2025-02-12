from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует список транзакций по указанному коду валюты и возвращает итератор.

    Параметры:
        transactions: Список словарей с информацией о транзакциях.
        currency_code: Код валюты (например, 'USD').

    Возвращает:
        Итератор по отфильтрованным транзакциям.

    Исключения:
        ValueError: Если `transactions` не является списком.
        ValueError: Если элементы `transactions` не являются словарями.
        ValueError: Если `currency_code` не является строкой.
        ValueError: Если `currency_code` пустой.
    """

    if not isinstance(transactions, list):
        raise ValueError("Транзакции должен быть списком")
    if not all(isinstance(item, dict) for item in transactions):
        raise ValueError("Каждая транзакция должна быть словарем")
    if not isinstance(currency_code, str):
        raise ValueError("Валюта операции (currency_code) должен быть строкой")
    if not currency_code.strip():
        raise ValueError("Валюта операции (currency_code) не может быть пустой")

    filtered_transactions = (
        item
        for item in transactions
        if item.get("operationAmount", {}).get("currency", {}).get("name", {}) == currency_code
    )
    return filtered_transactions


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    """
    Генерирует описания операций из списка транзакций.

    Параметры:
        transactions: Список словарей с информацией о транзакциях.

    Возвращает:
        Итератор, который возвращает описание каждой транзакции.

    Исключения:
        ValueError: Если `transactions` не является списком.
        ValueError: Если элементы `transactions` не являются словарями.
        ValueError: Если у транзакции отсутствует ключ 'description'.
    """

    if not isinstance(transactions, list):
        raise ValueError("Транзакции должен быть списком")
    if not all(isinstance(item, dict) for item in transactions):
        raise ValueError("Каждая транзакция должна быть словарем")
    if not all("description" in item for item in transactions):
        raise ValueError("Каждая транзакция должна содержать ключ 'description'")

    filtered_transactions = (item["description"] for item in transactions)
    return filtered_transactions


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    Параметры:
         start: Начальный номер диапазона (от 1 до 9999999999999999).
         end: Конечный номер диапазона (не более 9999999999999999).

    Возвращает:
         Итератор, выдающий номера карт в формате XXXX XXXX XXXX XXXX.
    Исключения:
         ValueError: Если `start` или `end` не являются целыми числами.
         ValueError: Если `start` или `end` выходят за пределы допустимого диапазона.
         ValueError: Если `start` больше `end`.
    """

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("start и end должны быть целыми числами")
    if start < 1 or end > 9999999999999999:
        raise ValueError("start и end должны быть в диапазоне от 1 до 9999999999999999")
    if start > end:
        raise ValueError("start не может быть больше end")

    card_numbers = (
        f"{str(num)[0:4]} {str(num)[4:8]} {str(num)[8:12]} {str(num)[12:16]}" for num in range(start, end + 1)
    )
    return card_numbers
