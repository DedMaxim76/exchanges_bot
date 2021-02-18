from sqlalchemy import Integer, Column, BigInteger, String, Float, sql, Boolean

from utils.db_api.db_gino import TimedBaseModel


class ExchangeRate(TimedBaseModel):
    __tablename__ = 'exchange_rate'
    id = Column(BigInteger, primary_key=True, unique=True)
    currency = Column(String(3))
    rate = Column(Float)

    query: sql.Select
