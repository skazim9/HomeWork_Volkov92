import json
from typing import Any
import logging
from src.external_api import convert_to_rub

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name) - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_info(path: str) -> list[Any] | Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info("Получаем список транзакций")
        with open(path, 'r', encoding='utf-8') as operations:
            try:
                transactions_data = json.load(operations)
                logger.info("Список транзакций готов")
                return transactions_data
            except json.JSONDecodeError:
                logger.error("Ошибка декодирования")
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        logger.error("Файл не найден")
        transactions_data = []
        return transactions_data


def transaction_in_rub(transactions: list, transaction_id: int) -> str | Any:
    """Принимает транзакцию и возвращает сумму в рублях, если операция не в рублях, конвертирует"""
    logger.info("Получаем сумму в рублях")
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                logger.info(f"Сумма операции в рублях:{rub_amount}")
                return rub_amount
            else:
                transaction_convert = dict()
                transaction_convert["amount"] = transaction["operationAmount"]["amount"]
                transaction_convert["currency"] = transaction["operationAmount"]["currency"]["code"]
                logger.info(f"Сумма в {transaction_convert["currency"]}:{transaction_convert["amount"]}")
                rub_amount = round(convert_to_rub(transaction_convert), 2)
                if rub_amount != 0:
                    logger.info(f"Сумма операции в рублях:{rub_amount}")
                    return rub_amount
                else:
                    logger.error("Конвертация не может быть выполнена")
                    return "Конвертация не может быть выполнена"
        else:
            return "Транзакция не найдена"

# transactions = get_transactions_info("../data/operations.json")
# print(transaction_in_rub(transactions, 441945886))
# print(get_transactions_info("../data/operations.json"))
