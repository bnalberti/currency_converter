import requests
import json
from logger_config import setup_logging

logger = setup_logging()

def get_exchange_rate(base: str, target: str, use_mock: bool = False) -> float:
    if use_mock:
        with open("data/mock_rates.json") as f:
            data = json.load(f)
        rate = data["rates"].get(target)
        if rate is None:
            raise ValueError(f"Currency {target} not found in mock data.")
        return rate
    else:
        url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"
        response = requests.get(url)
        if response.status_code != 200:
            raise ConnectionError("Failed to fetch rates from API.")
        data = response.json()
        return data["rates"][target]
