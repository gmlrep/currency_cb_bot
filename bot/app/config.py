import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class RedisSettings(BaseModel):
    host: str = os.getenv('REDIS_HOST')
    port: int = int(os.getenv('REDIS_PORT'))


class Settings(BaseSettings):
    bot_token: str = os.getenv('BOT_TOKEN')

    redis_settings: RedisSettings = RedisSettings()


settings = Settings()