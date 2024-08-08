from src.processing import filter_by_state, sort_by_date
from src.read_csv import get_data_from_csv
from src.read_xlsx import get_data_from_excel
from src.sort import list_transactions_sort_search
from src.utils import get_transactions_info
from src.widget import get_data, mask_account_card


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        item_number = input("Введите номер пункта: ")

        if item_number == "1":
            print("Для обработки выбран JSON-файл.")
            list_transactions = get_transactions_info("../data/operations.json")
            break
        elif item_number == "2":
            print("Для обработки выбран CSV-файл.")
            list_transactions = get_data_from_csv("../data/transactions.csv")
            break
        elif item_number == "3":
            print("Для обработки выбран XLSX-файл.")
            list_transactions = get_data_from_excel("../data/transactions_excel.xlsx")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    filters = []

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        ).upper()
        if status in ["CANCELED", "PENDING", "EXECUTED"]:
            filters.append(("status", status))
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        sort_date = input("Отсортировать операции по дате?  Да/Нет\n").lower()
        if sort_date == "да":
            sorting_order = input(
                """Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n"""
            ).lower()
            if sorting_order == "по возрастанию":
                filters.append(("date", False))
                break
            else:
                filters.append(("date", True))
                break
        elif sort_date == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        sort_code = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
        if sort_code == "да":
            filters.append(("currency", "RUB"))
            break
        elif sort_code == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if user_input == "да":
            search = input("Видите слово для поиска: ")
            filters.append(("description", search))
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    transactions = list_transactions
    for filter_type, filter_value in filters:
        if filter_type == "status":
            transactions = filter_by_state(transactions, filter_value)
        elif filter_type == "date":
            transactions = sort_by_date(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [txn for txn in transactions if txn["operationAmount"]["currency"]["code"] == filter_value]
        elif filter_type == "description":
            transactions = list_transactions_sort_search(transactions, filter_value)
    print("Распечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        if "from" in transaction:
            from_ = mask_account_card(transaction["from"])
        else:
            from_ = "0"
        to_ = mask_account_card(transaction["to"])
        date = get_data(transaction["date"])
        description = transaction["description"]
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]

        if description == "Открытие вклада":
            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
