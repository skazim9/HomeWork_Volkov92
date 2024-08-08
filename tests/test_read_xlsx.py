from unittest.mock import patch

import pandas as pd

from src.read_xlsx import get_data_from_excel


def test_read_xlsx_transactions():
    file_name = "test.xlsx"
    data = {
        "id": [1, 2],
        "state": ["success", "failed"],
        "date": ["2022-01-01", "2022-01-02"],
        "amount": [100, 200],
        "currency_name": ["USD", "EUR"],
        "currency_code": ["USD", "EUR"],
        "description": ["Test transaction", "Another transaction"],
        "from": ["Account 1", "Account 2"],
        "to": ["Account 2", "Account 3"],
    }
    df = pd.DataFrame(data)

    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = df
        result = get_data_from_excel(file_name)
        assert len(result) == 2
        assert result[0] == {
            "id": 1,
            "state": "success",
            "date": "2022-01-01",
            "operationAmount": {"amount": 100, "currency": {"name": "USD", "code": "USD"}},
            "description": "Test transaction",
            "from": "Account 1",
            "to": "Account 2",
        }
        assert result[1] == {
            "id": 2,
            "state": "failed",
            "date": "2022-01-02",
            "operationAmount": {"amount": 200, "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Another transaction",
            "from": "Account 2",
            "to": "Account 3",
        }
