from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.exchangeratesapi import Api

api_exchange = Api()


@dp.message_handler(Command(['list', 'lst']))
async def get_latest_exchange_rate(message: types.Message):
    list_exchange_rate = await api_exchange.get_latest_exchange_rate(base_currency="USD")
    rates: dict = list_exchange_rate['rates']
    result = '\n'.join([f'{key.capitalize()}: {round(value, 2)}' for key, value in rates.items()])

    await message.answer(text=result)