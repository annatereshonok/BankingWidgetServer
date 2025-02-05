from typing import Any, Dict, List


def filter_by_state(processed_info: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по заданному состоянию.

    Эта функция принимает список словарей, где каждый словарь содержит информацию о процессе.
    Она возвращает новый список, содержащий только те словари, в которых значение ключа
    'state' соответствует заданному состоянию.

    Параметры:
        processed_info (List[Dict[str, Any]]): Список словарей, содержащий информацию о процессах.
        state (str): Состояние, по которому будет производиться фильтрация.
                 По умолчанию используется значение 'EXECUTED'.

    Возвращает:
        List[Dict[str, Any]]: Список словарей, отфильтрованных по заданному состоянию.

    Исключения:
        ValueError: Если `processed_info` не является списком.
        ValueError: Если `processed_info` содержит не словари.
        ValueError: Если `state` не является строкой.
    """
    if not isinstance(processed_info, list):
        raise ValueError("Подаваемые данные должны быть списком словарей")

    for item in processed_info:
        if not isinstance(item, dict):
            raise ValueError("Каждый элемент в списке должен быть словарем")

    if not isinstance(state, str):
        raise ValueError("Состояние должно иметь строкое значение")

    filtered_info = [item for item in processed_info if item.get("state") == state]

    return filtered_info


def sort_by_date(processed_info: List[Dict[str, Any]], reverse_bool: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    Эта функция принимает список словарей, где каждый словарь содержит информацию о процессе,
    и сортирует его по значению ключа 'date'. Сортировка может быть выполнена в прямом или обратном порядке
    в зависимости от значения параметра `reverse_bool`.

    Параметры:
        processed_info (List[Dict[str, Any]]): Список словарей, содержащий информацию о процессах.
        reverse_bool (bool): Если True, сортировка будет выполнена в обратном порядке.
                            По умолчанию True (обратный порядок).

    Возвращает:
        List[Dict[str, Any]]: Отсортированный список словарей по дате.

    Исключения:
        ValueError: Если `processed_info` не является списком.
        ValueError: Если `processed_info` содержит элементы, которые не являются словарями.
        ValueError: Если отсутствует ключ 'date' в словарях.
        ValueError: Если значение 'date' не является строкой корректного формата.
        ValueError: Если `reverse_bool` не является булевым значением.
    """
    if not isinstance(processed_info, list):
        raise ValueError("Подаваемые данные должны быть списком словарей")

    for item in processed_info:
        if not isinstance(item, dict):
            raise ValueError("Каждый элемент в списке должен быть словарем")
        if "date" not in item:
            raise ValueError("Каждый словарь должен содержать ключ 'date'")
        if not isinstance(item["date"], str):
            raise ValueError("Значение 'date' должно быть строкой")

    if not isinstance(reverse_bool, bool):
        raise ValueError("Аргумент сортировки должен быть булевым значением")

    sorted_info = sorted(processed_info, key=lambda x: x["date"], reverse=reverse_bool)
    return sorted_info
