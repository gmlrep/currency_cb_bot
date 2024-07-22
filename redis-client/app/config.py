import os

from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class RedisSettings(BaseModel):
    host: str = os.getenv('REDIS_HOST')
    port: int = int(os.getenv('REDIS_PORT'))


class Settings(BaseSettings):

    hour: int = int(os.getenv('UPDATE_TIME').split(':')[0])
    minutes: int = int(os.getenv('UPDATE_TIME').split(':')[1])

    redis_settings: RedisSettings = RedisSettings()


settings = Settings()
