from src.search_transactions import search_transactions_category, search_transactions_key


def test_search_transactions_key(params_for_search_transactions_key):
    transactions, search_info, expected_results = params_for_search_transactions_key
    assert len(search_transactions_key(transactions, search_info)) == expected_results


def test_search_transactions_category(params_for_search_transactions_category):
    transactions, categories, expected_results = params_for_search_transactions_category
    assert search_transactions_category(transactions, categories) == expected_results
