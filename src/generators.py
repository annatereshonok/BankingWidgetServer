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
        raise ValueError("Транзакции должны быть списком словарей")
    if not all(isinstance(item, dict) for item in transactions):
        raise ValueError("Каждая транзакция должна быть словарем")
    if not isinstance(currency_code, str):
        raise ValueError("Валюта операции (currency_code) должна быть строкой")
    if not currency_code.strip():
        raise ValueError("Валюта операции (currency_code) не может быть пустой")

    filtered_transactions = (
        item
        for item in transactions
        if item.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency_code
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
        raise ValueError("Транзакции должны быть списком словарей")
    if not all(isinstance(item, dict) for item in transactions):
        raise ValueError("Каждая транзакция должна быть словарем")
    if not all("description" in item for item in transactions):
        raise ValueError("Каждая транзакция должна содержать ключ 'description'")

    filtered_transactions = (item["description"] for item in transactions)
    return filtered_transactions


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    Параметры:
         start: Начальный номер диапазона (от 1 до 9999999999999999).
         end: Конечный номер диапазона (не более 9999999999999999).

    Возвращает:
         Итератор, выдающий номера карт в формате XXXX XXXX XXXX XXXX.
    Исключения:
         ValueError: Если `start` или `stop` не являются целыми числами.
         ValueError: Если `start` или `stop` выходят за пределы допустимого диапазона.
         ValueError: Если `start` больше `stop`.
    """

    if not isinstance(start, int) or not isinstance(stop, int):
        raise ValueError("start и stop должны быть целыми числами")
    if start < 1 or stop > 9999999999999999:
        raise ValueError("start и stop должны быть в диапазоне от 1 до 9999999999999999")
    if start > stop:
        raise ValueError("start не может быть больше stop")

    card_numbers = (
        f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:]
        for num in range(start, stop + 1)
    )
    return card_numbers
