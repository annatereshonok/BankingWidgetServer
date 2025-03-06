import os
from typing import Any, Dict, List, Hashable

import pandas as pd

from src.logging_config import utils_logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_from_file(filepath: str, method: str) -> List[Dict[Hashable, Any]]:
    """
    Читает файл и возвращает список словарей с данными.

    Параметры:
        filepath (str): Путь к файлу.
        method (str): CSV или XLSX

    Возвращает:
        List[Dict[str, Any]]: Список транзакций в виде словарей.
        Если файл отсутствует или содержит некорректные данные, возвращает пустой список.
    """
    data_path = os.path.join(BASE_DIR, filepath)
    utils_logger.info(f"Попытка открыть файл: {filepath}")

    try:
        transactions = pd.DataFrame()

        if method == "csv":
            transactions = pd.read_csv(data_path, delimiter=";")
        elif method == "xlsx":
            transactions = pd.read_excel(data_path)

        if transactions.empty:
            utils_logger.warning(f"Файл {filepath} пуст.")
            return []

        utils_logger.info(f"Файл {filepath} успешно загружен. Найдено {len(transactions)} записей.")
        return transactions.to_dict(orient="records")

    except FileNotFoundError:
        utils_logger.error(f"Файл {filepath} не найден.")
        return []
    except (TypeError, ValueError, pd.errors.ParserError) as e:
        utils_logger.error(f"Ошибка обработки данных в файле {filepath}: {e}")
        return []


def read_from_csv(filepath: str) -> List[Dict[Hashable, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с данными.

    Параметры:
        filepath (str): Путь к CSV-файлу.

    Возвращает:
        List[Dict[str, Any]]: Список транзакций в виде словарей.
    """
    transactions = read_from_file(filepath=filepath, method="csv")
    return transactions


def read_from_xlsx(filepath: str) -> List[Dict[Hashable, Any]]:
    """
    Читает XLSX-файл и возвращает список словарей с данными.

    Параметры:
        filepath (str): Путь к XLSX-файлу.

    Возвращает:
        List[Dict[str, Any]]: Список транзакций в виде словарей.
    """
    transactions = read_from_file(filepath=filepath, method="xlsx")
    return transactions
