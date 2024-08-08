import re
from collections import Counter
from typing import Dict, List

# from src.utils import list_transactions


def list_transactions_sort_search(list_txn: List[dict], search_bar: str) -> List[dict]:
    """Функция, которая возвращает список словарей, у которых в описании есть строка поиска вводимая пользователем"""
    new_list_transactions = []
    for transactions in list_txn:
        if "description" in transactions and re.search(search_bar, transactions["description"], flags=re.IGNORECASE):
            new_list_transactions.append(transactions)
    return new_list_transactions


# if __name__ == "__main__":
#
#     search = input("Введите слово для поиска: ")
#     print(list_transactions_sort_search(list_transactions, search))


def list_transactions_sort_description(transactions: List[Dict], list_categories: List[str]) -> Dict[str, int]:
    """Функция, которая возвращает словарь, в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории"""
    list_categories_transaction = []
    for transaction in transactions:
        if "description" in transaction and transaction["description"] in list_categories:
            list_categories_transaction.append(transaction["description"])
    sort_transaction = Counter(list_categories_transaction)
    return dict(sort_transaction)
