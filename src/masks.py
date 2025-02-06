def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, отображая его в формате:
    XXXX XX** **** XXXX, где X — это цифра номера.

    Параметры:
        card_number (str): Номер карты в строковом формате.

    Возвращает:
        str: Замаскированный номер карты.
    """
    if not card_number or card_number.strip() == "":
        raise ValueError("Номер карты не может быть пустым")

    card_number = str(card_number).replace(" ", "")

    print(card_number)

    if not card_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр")

    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, отображая его в формате:
    **XXXX, где X — это цифра номера.

    Параметры:
        account_number (str): Номер счета в строковом формате.

    Возвращает:
        str: Замаскированный номер счета.
    """
    if not account_number or account_number.strip() == "":
        raise ValueError("Номер счета не может быть пустым")

    account_number = str(account_number).replace(" ", "")

    if not account_number.isdigit():
        raise ValueError("Номер счета должен состоять только из цифр")

    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")

    account_number = f"**{account_number[-4:]}"
    return account_number
