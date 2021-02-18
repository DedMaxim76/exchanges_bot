from utils.db_api.quick_commands import exchange_rate_quick_commands
from utils.exchangeratesapi import Api

api_exchange = Api()


async def load_rates_from_server():
    await exchange_rate_quick_commands.clear_table()
    list_exchange_rate = await api_exchange.get_latest_exchange_rate(base_currency="USD")
    rates: dict = list_exchange_rate['rates']
    for key, value in rates.items():
        await exchange_rate_quick_commands.add_rate(key.capitalize(), round(value, 2))
