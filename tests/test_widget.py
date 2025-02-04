import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card_positive(params_for_widget_mask_positive):
    card_number, expected_results = params_for_widget_mask_positive
    assert mask_account_card(card_number) == expected_results


def test_mask_account_card_negative(params_for_widget_mask_negative):
    card_number, expected_error = params_for_widget_mask_negative
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_number)
    assert str(exc_info.value) == expected_error
