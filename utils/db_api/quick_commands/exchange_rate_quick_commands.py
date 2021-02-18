from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.exchange_rate import ExchangeRate


async def add_rate(currency: str, rate: float):
    try:
        exchange_rate = ExchangeRate(currency=currency,
                                     rate=rate)
        await exchange_rate.create()
    except UniqueViolationError:
        pass


async def select_all_rates():
    rates = await ExchangeRate.query.gino.all()
    return rates


async def count_rates():
    total = await db.func.count(ExchangeRate.id).gino.scalar()
    return total


async def select_rate(currency: str):
    rate = await ExchangeRate.query.where(ExchangeRate.currency == currency).gino.first()
    if not rate:
        return None
    return rate


async def get_timestamp():
    rate = await ExchangeRate.get(1)
    if not rate:
        return None
    return rate.created_at.timestamp()


async def clear_table():
    await ExchangeRate.gino.drop()
    await ExchangeRate.gino.create()
