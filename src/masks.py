from src.decorators import log
from src.logging_config import masks_logger


@log(filename="log_masks.txt")
def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, отображая его в формате:
    XXXX XX** **** XXXX, где X — это цифра номера.

    Параметры:
        card_number (str): Номер карты в строковом формате.

    Возвращает:
        str: Замаскированный номер карты.
    """
    masks_logger.info(f"Вызов get_mask_card_number с аргументом: {card_number}")

    if not card_number or card_number.strip() == "":
        masks_logger.error("Номер карты не может быть пустым")
        raise ValueError("Номер карты не может быть пустым")

    card_number = str(card_number).replace(" ", "")

    if not card_number.isdigit():
        masks_logger.error("Номер карты должен состоять только из цифр")
        raise ValueError("Номер карты должен состоять только из цифр")

    if len(card_number) != 16:
        masks_logger.error("Номер карты должен содержать 16 цифр")
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    masks_logger.info(f"Функция get_mask_card_number успешно выполнена. Результат: {masked_number}")

    return masked_number


@log(filename=None)
def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, отображая его в формате:
    **XXXX, где X — это цифра номера.

    Параметры:
        account_number (str): Номер счета в строковом формате.

    Возвращает:
        str: Замаскированный номер счета.
    """
    masks_logger.info(f"Вызов get_mask_account с аргументом: {account_number}")

    if not account_number or account_number.strip() == "":
        masks_logger.error("Номер счета не может быть пустым")
        raise ValueError("Номер счета не может быть пустым")

    account_number = str(account_number).replace(" ", "")

    if not account_number.isdigit():
        masks_logger.error("Номер счета должен состоять только из цифр")
        raise ValueError("Номер счета должен состоять только из цифр")

    if len(account_number) != 20:
        masks_logger.error("Номер счета должен содержать 20 цифр")
        raise ValueError("Номер счета должен содержать 20 цифр")

    account_number = f"**{account_number[-4:]}"
    masks_logger.info(f"Функция get_mask_account успешно выполнена. Результат: {account_number}")

    return account_number


if __name__ == "__main__":
    print(get_mask_card_number(""))
