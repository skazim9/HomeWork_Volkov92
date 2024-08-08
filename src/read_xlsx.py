import pandas as pd


def get_data_from_excel(excel_file: str) -> list:
    """Считываем данные из excel файла и создаем список словарей"""
    try:
        excel_data = pd.read_excel(excel_file)
        transactions_list = excel_data.apply(
            lambda row: {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {
                        "name": row["currency_name"],
                        "code": row["currency_code"],
                    },
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            },
            axis=1,
        )
        new_dict_list = []
        row_index = 0
        for row in transactions_list:
            new_dict_list.append(transactions_list[row_index])
            row_index += 1
        return new_dict_list
    except Exception:
        return []
