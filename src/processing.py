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
