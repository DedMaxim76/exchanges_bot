import datetime
import os

import matplotlib.pyplot as plt

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.load_rates_from_server import api_exchange


@dp.message_handler(Command(['history']))
async def get_rates_history_graphic(message: types.Message):
    args = message.get_args()
    if len(args) == 0:
        await message.answer("You should insert params in command...")
        return
    args = args.split(' ')
    currence_map = args[0].partition('/')
    base_currency = currence_map[0]
    final_currency = currence_map[2]
    period = args[2]
    time_delta = datetime.timedelta(days=int(period))
    end_at = datetime.datetime.now().date()
    start_at = (end_at - time_delta)
    rates = await api_exchange.get_history_rates_by_delta(start_at=start_at,
                                                          end_at=end_at,
                                                          base_currency=base_currency,
                                                          final_currency=final_currency)
    if "error" in rates or rates['rates'] is None:
        await message.answer("No exchange rate data is available for the selected currency")
        return
    rates = rates['rates']
    y_data = []
    x_data = []
    for key, value in rates.items():
        x_data.append(key)
        y_data.append(float(value[final_currency]))
    x_data.sort()
    await lineplot(x_data=x_data,
                   y_data=y_data)
    await message.answer_photo(open('data/graphics/1.jpg', 'rb'))
    os.remove("data/graphics/1.jpg")  # if you don`t want to delete graphics after sending via bot comment this line


async def lineplot(x_data, y_data):
    fig, ax = plt.subplots()
    ax.plot(x_data, y_data)
    fig.savefig('data/graphics/1.jpg')
