import requests
import pandas as pd

def get_crypto_data():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"

        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 20,
            "page": 1,
            "sparkline": False
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        return pd.DataFrame(data)

    except Exception as e:
        print("Error:", e)
        return pd.DataFrame()