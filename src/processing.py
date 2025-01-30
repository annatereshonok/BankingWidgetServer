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
    """

    filtered_info = [item for item in processed_info if item.get("state") == state]
    return filtered_info


# processed = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
# print(filter_by_state(processed, state='CANCELED'))


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
    """

    sorted_info = sorted(processed_info, key=lambda x: x["date"], reverse=reverse_bool)
    return sorted_info


# processed = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
# print(sort_by_date(processed))
