from redis import asyncio as redis

from bot.config import settings
from bot.utils import get_currency_xml, get_pars_currency

client = redis.StrictRedis(
                host=settings.redis_settings.host,
                port=settings.redis_settings.port,
                decode_responses=True,
            )


async def set_currency():
    await get_currency_xml()
    currency = get_pars_currency()
    for cur in currency:
        await client.set(cur, str(currency[cur]))


async def get_all_currencies() -> dict:
    keys = await client.keys()
    currencies = {key: eval(await client.get(key)) for key in keys}
    print(currencies)
    return currencies


async def get_currency(valute_code: str) -> dict:
    data = await client.get(valute_code.upper())
    return eval(data)
