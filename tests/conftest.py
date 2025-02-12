import pytest


@pytest.fixture(params=[("7000792289606361", "7000 79** **** 6361"), ("1234 5678 9012 3456", "1234 56** **** 3456")])
def params_for_masks_card_positive(request):
    return request.param


@pytest.fixture(
    params=[
        ("", "Номер карты не может быть пустым"),
        ("   ", "Номер карты не может быть пустым"),
        ("700079228960636132", "Номер карты должен содержать 16 цифр"),
        ("1234-5678-9012-3456", "Номер карты должен состоять только из цифр"),
    ]
)
def params_for_masks_card_negative(request):
    return request.param


@pytest.fixture(params=[("73654108430135874305", "**4305"), ("7365 4108 4301 3587 4305", "**4305")])
def params_for_masks_account_positive(request):
    return request.param


@pytest.fixture(
    params=[
        ("", "Номер счета не может быть пустым"),
        ("   ", "Номер счета не может быть пустым"),
        ("700079228960636132", "Номер счета должен содержать 20 цифр"),
        ("1234-5678-9012-3456", "Номер счета должен состоять только из цифр"),
    ]
)
def params_for_masks_account_negative(request):
    return request.param


@pytest.fixture(
    params=[
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ]
)
def params_for_widget_mask_positive(request):
    return request.param


@pytest.fixture(
    params=[
        ("Maestro 73654108430135874305", "Номер карты должен содержать 16 цифр"),
        ("Visa Platinum 89909", "Номер карты должен содержать 16 цифр"),
        ("Счет 7365410843013587", "Номер счета должен содержать 20 цифр"),
        ("Счет 646864736788947795893880", "Номер счета должен содержать 20 цифр"),
        ("MasterCard 4000 1234 5678 3BCD", "Номер карты должен состоять только из цифр"),
        ("Счет 64686473678894779589AAAA", "Номер счета должен состоять только из цифр"),
        # ("Visa Platinum XXXX XXXX XXXX XXXX", "Номер карты должен состоять только из цифр"),
        ("", "Не введен номер карты/счета"),
        ("  ", "Не введен номер карты/счета"),
        ("1596837868705199", "Данные введены некорректно"),
        ("MasterCard", "Номер карты не может быть пустым"),
        ("Visa Platinum", "Номер карты не может быть пустым"),
        ("Счет ", "Номер счета не может быть пустым"),
    ]
)
def params_for_widget_mask_negative(request):
    return request.param


@pytest.fixture(
    params=[
        ("2024-02-03T15:30:45.123456", "03.02.2024"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2000-01-01T00:00:00.000000", "01.01.2000"),
    ]
)
def params_for_widget_date_positive(request):
    return request.param


@pytest.fixture(
    params=[
        ("", "Дата не может быть пустой"),
        ("   ", "Дата не может быть пустой"),
        (None, "Дата должна быть строкой"),
        (123456, "Дата должна быть строкой"),
        ([], "Дата должна быть строкой"),
        ("2024/02/03 15:30:45.123456", "Некорректный формат даты"),
        ("03-02-2024T15:30:45.123456", "Некорректный формат даты"),
        ("2024-02-03", "Некорректный формат даты"),
        ("15:30:45.123456", "Некорректный формат даты"),
        ("2024-02-03T15:30:45", "Некорректный формат даты"),
        ("2024-02-03T25:61:61.123456", "Некорректный формат даты"),
        ("abcd-ef-ghTij:kl:mn.opqrst", "Некорректный формат даты"),
    ]
)
def params_for_widget_date_negative(request):
    return request.param


@pytest.fixture(
    params=[
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            [
                {"id": 123, "state": "PENDING", "date": "2020-01-01T12:00:00.000000"},
            ],
            "EXECUTED",
            [],
        ),
        ([], "EXECUTED", []),
    ]
)
def params_for_processing_state_positive(request):
    return request.param


@pytest.fixture(
    params=[
        (None, "EXECUTED", "Подаваемые данные должны быть списком словарей"),
        (123, "EXECUTED", "Подаваемые данные должны быть списком словарей"),
        ("string", "EXECUTED", "Подаваемые данные должны быть списком словарей"),
        ({"id": 1, "state": "EXECUTED"}, "EXECUTED", "Подаваемые данные должны быть списком словарей"),
        ([{"id": 1, "state": "EXECUTED"}, 123], "EXECUTED", "Каждый элемент в списке должен быть словарем"),
        ([{"id": 1, "state": "EXECUTED"}, None], "EXECUTED", "Каждый элемент в списке должен быть словарем"),
        ([{"id": 1, "state": "EXECUTED"}], None, "Состояние должно иметь строкое значение"),
        ([{"id": 1, "state": "EXECUTED"}], 123, "Состояние должно иметь строкое значение"),
        ([{"id": 1, "state": "EXECUTED"}], ["EXECUTED"], "Состояние должно иметь строкое значение"),
    ]
)
def params_for_processing_state_negative(request):
    return request.param


@pytest.fixture(
    params=[
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        ([], True, []),
        ([], False, []),
    ]
)
def params_for_processing_date_positive(request):
    return request.param


@pytest.fixture(
    params=[
        (None, True, "Подаваемые данные должны быть списком словарей"),
        (123, True, "Подаваемые данные должны быть списком словарей"),
        ("string", True, "Подаваемые данные должны быть списком словарей"),
        ({"id": 1, "date": "2019-07-03T18:35:29.512364"}, True, "Подаваемые данные должны быть списком словарей"),
        (
            [{"id": 1, "date": "2019-07-03T18:35:29.512364"}, 123],
            True,
            "Каждый элемент в списке должен быть словарем",
        ),
        (
            [{"id": 1, "date": "2019-07-03T18:35:29.512364"}, None],
            True,
            "Каждый элемент в списке должен быть словарем",
        ),
        ([{"id": 1}], True, "Каждый словарь должен содержать ключ 'date'"),
        ([{"id": 1, "date": 123}], True, "Значение 'date' должно быть строкой"),
        ([{"id": 1, "date": "2019-07-03T18:35:29.512364"}], None, "Аргумент сортировки должен быть булевым значением"),
        ([{"id": 1, "date": "2019-07-03T18:35:29.512364"}], 123, "Аргумент сортировки должен быть булевым значением"),
    ]
)
def params_for_processing_date_negative(request):
    return request.param


@pytest.fixture
def transactions_example():
    data = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return data


@pytest.fixture
def transactions_example_no_desc():
    data = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    return data


@pytest.fixture(params=[0, 1, 2, 3])
def params_filter_by_currency_negative(request, transactions_example):
    test_cases = [
        ("", "", "Транзакции должны быть списком словарей"),
        ([[], {}], "", "Каждая транзакция должна быть словарем"),
        (transactions_example, 1, "Валюта операции (currency_code) должна быть строкой"),
        (transactions_example, "", "Валюта операции (currency_code) не может быть пустой"),
    ]
    return test_cases[request.param]


@pytest.fixture(params=[0, 1, 2])
def params_transaction_descriptions_negative(request, transactions_example_no_desc):
    test_cases = [
        ("", "Транзакции должны быть списком словарей"),
        ([[], {}], "Каждая транзакция должна быть словарем"),
        (transactions_example_no_desc, "Каждая транзакция должна содержать ключ 'description'"),
    ]
    return test_cases[request.param]


@pytest.fixture(
    params=[
        ("1", "100", "start и end должны быть целыми числами"),
        (0, 1, "start и end должны быть в диапазоне от 1 до 9999999999999999"),
        (10, 5, "start не может быть больше end"),
    ],
)
def params_card_number_generator_negative(request):
    return request.param
