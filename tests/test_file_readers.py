import os
from unittest.mock import patch

import pandas as pd

from src.file_readers import read_from_csv, read_from_xlsx

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@patch("src.file_readers.pd.read_csv")
def test_read_from_csv_success(mock_read_csv):
    mock_df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    mock_read_csv.return_value = mock_df

    result = read_from_csv("data.csv")
    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


@patch("src.file_readers.pd.read_csv")
def test_read_from_csv_invalid_structure(mock_read_csv):
    mock_df = pd.DataFrame([])
    mock_read_csv.return_value = mock_df

    result = read_from_csv("data.csv")
    assert result == []


@patch("src.file_readers.pd.read_csv", side_effect=FileNotFoundError)
def test_read_from_csv_file_not_found(mock_file):
    assert read_from_csv("missing_file.csv") == []


@patch("src.file_readers.pd.read_csv", side_effect=TypeError)
def test_read_from_csv_typeerror(mock_file):
    assert read_from_csv("dummy_path.csv") == []


@patch("src.file_readers.pd.read_csv", side_effect=pd.errors.ParserError)
def test_read_from_csv_parsing_error(mock_file):
    assert read_from_csv("dummy_path.xlsx") == []


@patch("src.file_readers.pd.read_excel")
def test_read_from_xlsx_success(mock_read_csv):
    mock_df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    mock_read_csv.return_value = mock_df

    result = read_from_xlsx("data.xlsx")
    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


@patch("src.file_readers.pd.read_excel")
def test_read_from_xlsx_invalid_structure(mock_read_csv):
    mock_df = pd.DataFrame([])
    mock_read_csv.return_value = mock_df

    result = read_from_xlsx("data.xlsx")
    assert result == []


@patch("src.file_readers.pd.read_excel", side_effect=FileNotFoundError)
def test_read_from_xlsx_file_not_found(mock_file):
    assert read_from_xlsx("missing_file.xlsx") == []


@patch("src.file_readers.pd.read_excel", side_effect=TypeError)
def test_read_from_xlsx_typeerror(mock_file):
    assert read_from_xlsx("dummy_path.xlsx") == []


@patch("src.file_readers.pd.read_excel", side_effect=pd.errors.ParserError)
def test_read_from_xlsx_parsing_error(mock_file):
    assert read_from_xlsx("dummy_path.xlsx") == []
