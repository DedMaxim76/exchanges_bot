from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.exchangeratesapi import Api

api_exchange = Api()


@dp.message_handler(Command(["test"]))
async def test(message: types.Message):
    response = await api_exchange.get_history_rates_by_delta(start_at="2019-11-27",
                                                             end_at="2019-12-27",
                                                             base_currency="USD",
                                                             final_currency="CAD")
    await message.answer(response)
