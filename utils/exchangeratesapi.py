import requests_async as requests

API_URL = "https://api.exchangeratesapi.io"


class Api:
    def __init__(self):
        pass

    async def _query(self, params, url):
        response = await requests.get(url, params=params)
        print(response.url)
        return response.json()

    async def get_currency_rate(self, base_currency, final_currency):
        url = API_URL + "/latest"
        params = {
            "base": base_currency,
            "symbols": final_currency,
        }
        response = await self._query(params=params,
                                     url=url)
        return response

    async def get_latest_exchange_rate(self, base_currency):
        url = API_URL + "/latest"
        params = {
            "base": base_currency,
        }
        response = await self._query(params=params,
                                     url=url)
        return response

    async def get_history_rates_by_delta(self, start_at, end_at, base_currency, final_currency):
        url = API_URL + "/history"
        params = {
            'start_at': start_at,
            'end_at': end_at,
            'base': base_currency,
            'symbols': final_currency,
        }
        response = await self._query(params=params,
                                     url=url)
        return response
