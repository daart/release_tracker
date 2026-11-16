from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_port: int
    db_port: int

    postgres_db: str
    postgres_user: str
    postgres_password: str

    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="forbid",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()