import pytest
from unittest.mock import mock_open, patch
from src.read_xlsx import get_data_from_excel

PATH_EXCEL = "test_transactions_excel.xlsx"


def test_get_data_from_excel():
    assert get_data_from_excel(PATH_EXCEL) == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": 16210, "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": 29740, "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]
    assert get_data_from_excel("") == []


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
def test_get_data_from_excel(mock_file):
    result = get_data_from_excel("dummy.csv")
    assert result == expected_result

@patch("builtins.open", side_effect=Exception)
def test_get_data_from_excel_exception(mock_file):
    result = get_data_from_excel("dummy.csv")
    assert result == []