from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api import db_gino
from utils.db_api.db_gino import db
from utils.load_rates_from_server import load_rates_from_server
from utils.notify_admins import on_startup_notify


async def clear_table():
    print("Чистим базу")
    await db.gino.drop_all()
    print("Готово")
    print("Создаем таблицы")
    await db.gino.create_all()
    print("Готово")


async def on_startup(dispatcher):
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")
    # await clear_table()
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    await load_rates_from_server()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
