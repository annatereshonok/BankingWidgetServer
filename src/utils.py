import json
from typing import Any, Dict, List


def read_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Загружает финансовые транзакции из JSON-файла.

    Параметры:
        filepath: Путь к JSON-файлу.
    Возвращает:
        Список словарей с данными о транзакциях.

    Если файл отсутствует, пуст или содержит неверные данные, возвращается пустой список.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            transactions = json.load(file)

        if not isinstance(transactions, list):
            return []
        return transactions

    except (json.JSONDecodeError, TypeError, ValueError):
        return []

    except (FileNotFoundError, OSError):
        return []
