from pydantic_settings import BaseSettings

from functools import lru_cache


class Settings(BaseSettings):
    PORT: int = 8000
    HOST: str = '0.0.0.0'
    RELOAD: bool = False

    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_DB: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
