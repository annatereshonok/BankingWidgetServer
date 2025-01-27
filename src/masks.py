from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Маскирует номер кредитной карты, отображая его в формате:
    XXXX XX** **** XXXX, где X — это цифра номера.

    Параметры:
    card_number (str): Номер карты в строковом формате.

    Возвращает:
    str: Замаскированный номер карты.
    """
    card_number = str(card_number).replace(" ", "")
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Маскирует номер счета, отображая его в формате:
    **XXXX, где X — это цифра номера.

    Параметры:
    account_number (str): Номер счета в строковом формате.

    Возвращает:
    str: Замаскированный номер счета.
    """
    account_number = str(account_number).replace(" ", "")
    account_number = f"**{account_number[-4:]}"
    return account_number


# print(get_mask_card_number("7000792289606361"))
# print(get_mask_account("73654108430135874305"))
