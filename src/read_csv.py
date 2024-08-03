import csv


def get_data_from_csv(csv_file: str) -> list:
    """Считываем данные из csv файла и создаем список словарей"""
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_data = csv.reader(file, delimiter=';')
            # next(csv_data)
            transactions_list = []
            for row in csv_data:
                if row:
                    id_, state, date, amount, currency_name, currency_code, from_, to, description = row
                    transactions_list.append(
                        {
                            "id": str(id_),
                            "state": state,
                            "date": date,
                            "operationAmount": {
                                "amount": str(amount),
                                "currency": {"name": currency_name, "code": currency_code},
                            },
                            "description": description,
                            "from": from_,
                            "to": to,
                        }
                    )
    except Exception:
        return []
    return transactions_list
