import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.config import settings
from app.redis_client import set_currency


async def main():

    logging.basicConfig(
        level=logging.INFO,
        # filename='data/logs.log',
        format="%(asctime)s - %(name)s - %(message)s",
    )

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.start()
    await set_currency()
    scheduler.add_job(set_currency, 'cron', hour=settings.hour, minute=settings.minutes)
    while True:
        pass

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
