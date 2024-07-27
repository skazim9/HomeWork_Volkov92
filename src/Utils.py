import json
from typing import Any, List
from src.external_api import convert_to_rub


def get_transactions_info(path: str) -> list[Any] | Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, 'r', encoding='utf-8') as operations:
            try:
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data


def transaction_in_rub(transactions: list, transaction_id: int) -> str | Any:
    """Принимает транзакцию и возвращает сумму в рублях, если операция не в рублях, конвертирует"""
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                return rub_amount
            else:
                transaction_convert = dict()
                transaction_convert["amount"] = transaction["operationAmount"]["amount"]
                transaction_convert["currency"] = transaction["operationAmount"]["currency"]["code"]
                rub_amount = round(convert_to_rub(transaction_convert), 2)
                if rub_amount != 0:
                    return rub_amount
                else:
                    return "Конвертация не может быть выполнена"
        else:
            return "Транзакция не найдена"