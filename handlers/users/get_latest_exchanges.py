import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api.db_gino import db
from utils.db_api.quick_commands import exchange_rate_quick_commands
from utils.load_rates_from_server import api_exchange, load_rates_from_server


@dp.message_handler(Command(['list', 'lst']))
async def get_latest_exchange_rate(message: types.Message):
    timestamp_past = await exchange_rate_quick_commands.get_timestamp()
    timestamp_now = datetime.datetime.now().timestamp()
    if timestamp_now - timestamp_past > datetime.timedelta(minutes=10).total_seconds():
        await load_rates_from_server()
    result = await get_rates_from_db()
    await message.answer(text=result)


async def get_rates_from_db():
    rates = await exchange_rate_quick_commands.select_all_rates()
    result = '\n'.join([f'{rate.currency}: {rate.rate}' for rate in rates])
    return result