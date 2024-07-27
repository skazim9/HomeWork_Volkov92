import requests
from typing import Any
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


class RequestException:
    pass


def convert_to_rub(transaction_convert: dict) -> Any:
    amount = transaction_convert["amount"]
    currency = transaction_convert["currency"]
    """Принимает значение в долларах или евро, обращается к внешнему API и возвращает конвертацию в рубли"""
    try:
        if currency == "USD":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
        elif currency == "EUR":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
    except RequestException:
        return 0
