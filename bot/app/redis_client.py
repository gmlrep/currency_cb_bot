import asyncio
import json

from app.config import settings
from redis import asyncio as redis


client = redis.StrictRedis(
                host=settings.redis_settings.host,
                port=settings.redis_settings.port,
                decode_responses=True,
            )


async def get_all_currencies() -> dict:
    currency = await client.hgetall('currency')
    currencies = {key: json.loads(currency[key]) for key in currency}
    return currencies


async def get_currency(valute_from: str, valute_to: str = "RUB") -> float:
    value_from = await client.hget('currency', key=valute_from.upper())
    if valute_to.upper() != 'RUB':
        value_to = await client.hget('currency', key=valute_to.upper())
        currency = float(json.loads(value_to)['value']) / float(json.loads(value_from)['value'])
        return currency
    return json.loads(value_from)['value']
