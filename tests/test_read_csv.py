from src.read_csv import get_data_from_csv

PATH_CSV = "test_transactions_csv.csv"


def test_get_data_from_csv():
    assert get_data_from_csv(PATH_CSV) == [
        {
            "id": "5515847",
            "state": "EXECUTED",
            "date": "2021-08-30T06:11:23Z",
            "operationAmount": {"amount": "18687", "currency": {"name": "Euro", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Mastercard 3924599516675344",
            "to": "Visa 4023206149439133",
        },
        {
            "id": "308178",
            "state": "EXECUTED",
            "date": "2020-09-07T17:16:11Z",
            "operationAmount": {"amount": "17368", "currency": {"name": "Zloty", "code": "PLN"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 2547099241263746",
            "to": "Discover 1506530746937020",
        }
    ]
    assert get_data_from_csv("") == []