import pytest
from unittest.mock import mock_open, patch
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


# @patch('csv.reader')
# def test_get_data_from_csv(mock_reader):
#     # Настраиваем mock_reader чтобы он возвращал нужный результат
#     mock_reader.return_value = iter([
#     ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
#     ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'SoL', 'PEN', 'Счет 58803664651298323391', 'Счет 39746506635466619397', 'Перевод организации']
#     ])
#
#     result = get_data_from_csv(os.path.join('path_to_data', 'transactions.csv'))
#     expected_result = [
#         {
#             "id": "650703",
#             "state": "EXECUTED",
#             "date": "2023-09-05T11:30:32Z",
#             "amount": "16210",
#             "currency_name": "SoL",
#             "currency_code": "PEN",
#             "from": "Счет 58803664651298323391",
#             "to": "Счет 39746506635466619397",
#             "description": "Перевод организации"
#         }
#     ]
#     assert result == expected_result

csv_data = (
    "1;COMPLETED;2021-08-01;100.00;USD;840;Account1;Account2;Payment for services\n"
    "2;PENDING;2021-08-02;200.00;EUR;978;Account3;Account4;Payment for goods\n"
)

expected_result = [
    {
        "id": "1",
        "state": "COMPLETED",
        "date": "2021-08-01",
        "operationAmount": {
            "amount": "100.00",
            "currency": {"name": "USD", "code": "840"},
        },
        "description": "Payment for services",
        "from": "Account1",
        "to": "Account2",
    },
    {
        "id": "2",
        "state": "PENDING",
        "date": "2021-08-02",
        "operationAmount": {
            "amount": "200.00",
            "currency": {"name": "EUR", "code": "978"},
        },
        "description": "Payment for goods",
        "from": "Account3",
        "to": "Account4",
    },
]

@patch("builtins.open", new_callable=mock_open, read_data=csv_data)
def test_get_data_from_csv(mock_file):
    result = get_data_from_csv("dummy.csv")
    assert result == expected_result

@patch("builtins.open", side_effect=Exception)
def test_get_data_from_csv_exception(mock_file):
    result = get_data_from_csv("dummy.csv")
    assert result == []
