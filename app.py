from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api import db_gino
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
