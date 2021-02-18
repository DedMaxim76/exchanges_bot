from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.exchangeratesapi import Api
from utils.load_rates_from_server import api_exchange


@dp.message_handler(Command(['exchange']))
async def exchange_money(message: types.Message):
    args = message.get_args()
    if len(args) == 0:
        await message.answer(text="You should insert params in command...")
        return
    args = args.split(' ')
    amount = float(args[0])
    base_currency = args[1]
    final_currency = args[3]
    rate = await api_exchange.get_currency_rate(base_currency,final_currency)
    final_amount = amount * rate['rates'][final_currency]
    await message.answer(text=f"You would receive {round(final_amount, 2)} {final_currency}")
