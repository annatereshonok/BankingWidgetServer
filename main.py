import re

from src.file_readers import read_from_csv, read_from_xlsx
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search_transactions import search_transactions_key
from src.utils import read_json
from src.widget import get_date, mask_account_card

DATA_PATH = {
    "JSON": "data/operations.json",
    "CSV": "data/transactions.csv",
    "XLSX": "data/transactions_excel.xlsx",
}
STATUSES = ["CANCELED", "PENDING", "EXECUTED"]


def main() -> None:
    """
    Главная функция программы, обрабатывающая банковские транзакции.
    Позволяет пользователю загружать, фильтровать, сортировать
    и выводить транзакции из разных источников (JSON, CSV, XLSX).
    """

    choice_map = {
        "1": "Для обработки выбран JSON-файл.\n",
        "2": "Для обработки выбран CSV-файл.\n",
        "3": "Для обработки выбран XLSX-файл.\n",
    }
    choice_read = input(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n"""
    ).strip()
    print(choice_map[choice_read])
    transactions: list = []
    if choice_read == "1":
        transactions = read_json(DATA_PATH["JSON"])
    elif choice_read == "2":
        transactions = read_from_csv(DATA_PATH["CSV"])
    elif choice_read == "3":
        transactions = read_from_xlsx(DATA_PATH["XLSX"])

    while True:
        choice_state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        ).strip()
        if choice_state in STATUSES:
            transactions = filter_by_state(transactions, choice_state.upper())
            print(f'Операции отфильтрованы по статусу "{choice_state}"\n')
            break
        else:
            print(f'Статус операции "{choice_state}" недоступен.\n')
            continue

    map_bool = {"да": True, "нет": False}
    map_sort = {"по возрастанию": False, "по убыванию": True}

    while True:
        choice_sort = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if choice_sort in map_bool:
            if map_bool[choice_sort]:
                while True:
                    choice_sort_direction = input("Отсортировать по возрастанию или по убыванию?\n").strip()
                    if choice_sort_direction in map_sort:
                        transactions = sort_by_date(
                            processed_info=transactions, reverse_bool=map_sort[choice_sort_direction]
                        )
                        break
                    else:
                        print("Ответ может быть только по возрастанию или по убыванию.\n")
                        continue
            break
        else:
            print("Ответ может быть только Да или Нет.")
            continue

    while True:
        choice_curr = input("Выводить только рублевые тразакции? Да/Нет\n").strip().lower()
        if choice_curr in map_bool:
            if map_bool[choice_curr]:
                transactions = filter_by_currency(transactions, currency_code="RUB")
            break
        else:
            print("Ответ может быть только Да или Нет.")
            continue

    while True:
        choice_sort_desc = (
            input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n""").strip().lower()
        )
        if choice_sort_desc in map_bool:
            if map_bool[choice_sort_desc]:
                search_info = input("Введите слово\n").strip().lower()
                transactions = search_transactions_key(transactions, search_info=search_info)
            break
        else:
            print("Ответ может быть только Да или Нет.")
            continue

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(list(transactions))}")

    for transaction in transactions:
        date = get_date(transaction.get("date"))
        description = transaction.get("description")
        if choice_read == "1":
            currency = transaction.get("operationAmount").get("currency").get("name")
            amount = transaction.get("operationAmount").get("amount")
        else:
            currency = transaction.get("currency_name")
            amount = transaction.get("amount")
        masked_to = mask_account_card(transaction.get("to"))
        masked_from = ""
        if not re.match("открытие", description, flags=re.I):
            masked_from = mask_account_card(transaction.get("from"))
            masked_to = " -> " + masked_to

        print(f"{date} {description}\n{masked_from}{masked_to}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
