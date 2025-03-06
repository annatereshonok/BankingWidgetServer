import json
import os
from typing import Any, Dict, List

from src.logging_config import utils_logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Загружает финансовые транзакции из JSON-файла.

    Параметры:
        filepath: Путь к JSON-файлу.
    Возвращает:
        Список словарей с данными о транзакциях.

    Если файл отсутствует, пуст или содержит неверные данные, возвращается пустой список.
    """
    data_path = os.path.join(BASE_DIR, filepath)
    utils_logger.info(f"Попытка открыть файл: {filepath}")

    try:
        with open(data_path, "r", encoding="utf-8") as file:
            transactions = json.load(file)

        if not isinstance(transactions, list):
            utils_logger.warning(f"Файл {filepath} не содержит список транзакций.")
            return []

        utils_logger.info(f"Файл {filepath} успешно загружен. Найдено {len(transactions)} записей.")
        return transactions

    except FileNotFoundError:
        utils_logger.error(f"Файл {filepath} не найден.")
    except json.JSONDecodeError:
        utils_logger.error(f"Файл {filepath} содержит неверные данные (ошибка JSON).")
    except (TypeError, ValueError) as e:
        utils_logger.error(f"Ошибка обработки данных в файле {filepath}: {e}")

    return []
