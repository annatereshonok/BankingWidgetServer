import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_positive(params_for_widget_mask_positive):
    card_number, expected_results = params_for_widget_mask_positive
    assert mask_account_card(card_number) == expected_results


def test_mask_account_card_negative(params_for_widget_mask_negative):
    card_number, expected_error = params_for_widget_mask_negative
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_number)
    assert str(exc_info.value) == expected_error


def test_get_date_positive(params_for_widget_date_positive):
    date, expected_results = params_for_widget_date_positive
    assert get_date(date) == expected_results


def test_get_date_negative(params_for_widget_date_negative):
    date, expected_error = params_for_widget_date_negative
    with pytest.raises(ValueError) as exc_info:
        get_date(date)
    assert str(exc_info.value) == expected_error
