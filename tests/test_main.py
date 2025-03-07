from unittest.mock import patch

from main import main

INPUTS = {
    "test_main_json": iter(["1", "EXECUTED", "нет", "нет", "нет"]),
    "test_main_invalid_status": iter(["1", "ЧТО-ТО", "EXECUTED", "нет", "нет", "нет"]),
    "test_main_sort_descending": iter(["1", "EXECUTED", "да", "по убыванию", "нет", "нет"]),
}


@patch("builtins.print")
@patch("builtins.input", side_effect=INPUTS["test_main_json"])
def test_main_json(mock_input, mock_print):
    main()

    assert any("Для обработки выбран JSON-файл." in call.args[0] for call in mock_print.call_args_list)
    assert any("Операции отфильтрованы по статусу" in call.args[0] for call in mock_print.call_args_list)


@patch("builtins.print")
@patch("builtins.input", side_effect=INPUTS["test_main_invalid_status"])
def test_main_invalid_status(mock_input, mock_print):
    main()
    assert any('Статус операции "ЧТО-ТО" недоступен.' in call.args[0] for call in mock_print.call_args_list)


@patch("builtins.print")
@patch("builtins.input", side_effect=INPUTS["test_main_sort_descending"])
def test_main_sort_descending(mock_input, mock_print):
    main()
    assert any("Отсортировать по возрастанию" in call.args[0] for call in mock_input.call_args_list)
