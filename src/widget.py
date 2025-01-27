from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


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

    account_splitted = account.split()
    account_number = account_splitted.pop()

    if len(account_number) < 20:
        masked_account = get_mask_card_number(account_number)
    else:
        masked_account = get_mask_account(account_number)

    full_masked_account = " ".join(account_splitted + [masked_account])
    return full_masked_account


# print(mask_account_card('Maestro 1596837868705199'))
# print(mask_account_card('Счет 64686473678894779589'))
# print(mask_account_card('MasterCard 7158300734726758'))
# print(mask_account_card('Счет 35383033474447895560'))
# print(mask_account_card('Visa Platinum 8990922113665229'))
# print(mask_account_card('Visa Gold 5999414228426353'))
# print(mask_account_card('Счет 73654108430135874305'))


def get_date(date: str) -> str:
    date_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date


# print(get_date("2024-03-11T02:26:18.671407"))
