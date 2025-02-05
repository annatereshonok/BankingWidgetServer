import pytest

from src.processing import filter_by_state, sort_by_date


def test_pocessing_state_positive(params_for_processing_state_positive):
    input_data, state, expected_results = params_for_processing_state_positive
    assert filter_by_state(input_data, state) == expected_results


def test_pocessing_state_negative(params_for_processing_state_negative):
    input_data, state, expected_exception_message = params_for_processing_state_negative
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(input_data, state)
    assert str(exc_info.value) == expected_exception_message


def test_pocessing_date_positive(params_for_processing_date_positive):
    input_data, reverse_bool, expected_results = params_for_processing_date_positive
    assert sort_by_date(input_data, reverse_bool) == expected_results


def test_pocessing_date_negative(params_for_processing_date_negative):
    input_data, reverse_bool, expected_exception_message = params_for_processing_date_negative
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(input_data, reverse_bool)
    assert str(exc_info.value) == expected_exception_message
