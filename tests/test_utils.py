import json
import os
from unittest.mock import mock_open, patch

from src.utils import read_json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_read_json_success(mock_file):
    expected_result = [{"id": 1, "amount": 100}]
    assert read_json("dummy_path.json") == expected_result
    data_path = os.path.join(BASE_DIR, "dummy_path.json")
    mock_file.assert_called_once_with(data_path, "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="{}")
def test_read_json_invalid_structure(mock_file):
    assert read_json("dummy_path.json") == []


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_json_empty_file(mock_file):
    assert read_json("dummy_path.json") == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_json_file_not_found(mock_file):
    assert read_json("missing_file.json") == []


@patch("builtins.open", new_callable=mock_open, read_data="[{'id': 1, 'amount': 100}]")
def test_read_json_invalid_json(mock_json_load):
    assert read_json("dummy_path.json") == []
    mock_json_load.assert_called_once()


@patch("builtins.open", side_effect=json.JSONDecodeError)
def test_read_json_error(mock_file):
    assert read_json("dummy_path.json") == []
