import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_positive(params_for_masks_card_positive):
    card_number, expected_results = params_for_masks_card_positive
    assert get_mask_card_number(card_number) == expected_results


def test_get_mask_card_number_negative(params_for_masks_card_negative):
    card_number, expected_error = params_for_masks_card_negative
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
    assert str(exc_info.value) == expected_error


def test_get_mask_account_positive(params_for_masks_account_positive):
    account_number, expected_results = params_for_masks_account_positive
    assert get_mask_account(account_number) == expected_results


def test_get_mask_account_negative(params_for_masks_account_negative):
    account_number, expected_error = params_for_masks_account_negative
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)
    assert str(exc_info.value) == expected_error
