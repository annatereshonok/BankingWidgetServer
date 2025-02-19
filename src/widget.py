from datetime import datetime

from src.decorators import log
from src.masks import get_mask_account, get_mask_card_number


@log(filename=None)
def mask_account_card(account: str) -> str:
    """
    Маскирует номер кредитной карты/счета, отображая его в формате:
        Для карт: [Название карты] XXXX XX** **** XXXX, где X — это цифра номера
        Для счетов: Счет **XXXX, где X — это цифра номера.

    Параметры:
        account (str): Номер карты/счета в строковом формате.

    Возвращает:
        str: Замаскированный номер карты/счета.
    """

    if not account or account.strip() == "":
        raise ValueError("Не введен номер карты/счета")

    if account.isdigit():
        raise ValueError("Данные введены некорректно")

    account_split = [item.strip() for item in account.split()]
    account_name_list = [item for item in account_split if item.isalpha()]
    account_name = " ".join(account_name_list)
    account_number = " ".join([item for item in account_split if item not in account_name_list]) or ""

    if account_name == "Счет":
        masked_account = get_mask_account(account_number)
    else:
        masked_account = get_mask_card_number(account_number)

    full_masked_account = " ".join([account_name, masked_account])
    return full_masked_account


@log(filename="log_widget.txt")
def get_date(date: str) -> str:
    """
    Преобразует дату из формата ISO 8601 ("YYYY-MM-DDTHH:MM:SS.ssssss") в формат "DD.MM.YYYY".

    Параметры:
        date (str): Дата в формате "YYYY-MM-DDTHH:MM:SS.ssssss".

    Возвращает:
        str: Дата в формате "DD.MM.YYYY".

    Raises:
        ValueError: Если передано не строковое значение.
        ValueError: Если строка пустая или содержит только пробелы.
        ValueError: Если дата не соответствует формату "YYYY-MM-DDTHH:MM:SS.ssssss".
    """
    if not isinstance(date, str):
        raise ValueError("Дата должна быть строкой")

    if not date.strip():
        raise ValueError("Дата не может быть пустой")

    try:
        date_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_object.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты")
