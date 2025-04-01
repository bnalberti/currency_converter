"""
Retrieves the exchange rates
"""
import requests
import json
from logger_config import setup_logging

logger = setup_logging()

def get_exchange_rate(base: str, target: str, use_mock: bool = False) -> float:
    if use_mock:
        with open("data/mock_rates.json") as f:
            data = json.load(f)

        mock_base = data["base"]
        rates = data["rates"]

        if base == mock_base:
            rate = rates.get(target)
        else:
            if base not in rates or target not in rates:
                raise ValueError(f"One of the currencies ({base}, {target}) not found in mock data.")
            rate = rates[target] / rates[base]  

        if rate is None:
            raise ValueError(f"Currency {target} not found in mock data.")
        
        return rate

    else:
        api_key = "erx15hpKb2dQdaWxycVOC4LqIK3sRJYI"
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={target}&base={base}"

        payload = {}
        headers= {
        "apikey": api_key
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.text
        
        if status_code != 200:
            raise ConnectionError(f"Failed to fetch rates from API. Status code: {status_code} - {result}")

        data = response.json()

        rate = data.get("rates", {}).get(target)
        if rate is None:
            raise ValueError(f"Currency {target} not found in API response.")

        return rate
