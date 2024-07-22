import asyncio
import json

from app.config import settings
from redis import asyncio as redis

from app.utils import get_pars_currency

client = redis.StrictRedis(
                host=settings.redis_settings.host,
                port=settings.redis_settings.port,
                decode_responses=True,
            )


async def set_currency():
    currency = await get_pars_currency()
    await client.hset('currency', mapping=currency)
