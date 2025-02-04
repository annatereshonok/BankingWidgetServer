from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


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
    # ("Cчет", "Номер счета не может быть пустым"),
    if not account or account.strip() == "":
        raise ValueError("Не введен номер карты/счета")

    if account.isdigit():
        raise ValueError("Данные введены некорректно")

    account_splitted = [item.strip() for item in account.split()]
    account_name_list = [item for item in account_splitted if item.isalpha()]
    account_name = ' '.join(account_name_list)
    account_number = ' '.join([item for item in account_splitted if item not in account_name_list]) or ""

    if account_name == 'Счет':
        masked_account = get_mask_account(account_number)
    else:
        masked_account = get_mask_card_number(account_number)

    full_masked_account = " ".join([account_name, masked_account])
    return full_masked_account


def get_date(date: str) -> str:
    date_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date

