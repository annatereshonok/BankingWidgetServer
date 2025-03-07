import re
from collections import Counter
from typing import Any, Dict, List


def search_transactions_key(transactions: List[Dict[str, Any]], search_info: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций, оставляя только те, в которых описание соответствует поисковому запросу.

    Параметры:
        transactions (List[Dict[str, Any]]): Список транзакций, где каждая транзакция представлена словарем.
        search_info (str): Строка поиска (регулярное выражение).

    Возвращает:
        List[Dict[str, Any]]: Список транзакций, удовлетворяющих поисковому запросу.
    """
    filtered_transactions = [
        t
        for t in transactions
        if isinstance(t.get("description", ""), str)
        and re.search(search_info, t.get("description", "").lower(), flags=re.I)
    ]
    return filtered_transactions


def search_transactions_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[Any, int]:
    """
    Подсчитывает количество операций в каждой категории.

    Параметры:
        transactions (List[Dict[str, str]]): Список словарей с банковскими операциями.
        categories (List[str]): Список категорий операций.

    Возвращает:
        Dict[str, int]: Словарь, где ключи — категории, значения — количество операций.
    """
    filtered_transactions = [
        t.get("description")
        for t in transactions
        if t.get("description", "").lower() in list(map(lambda x: x.lower(), categories))
    ]
    counted_categories = dict(Counter(filtered_transactions))
    return counted_categories
