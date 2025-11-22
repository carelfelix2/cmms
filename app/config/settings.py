from pydantic import BaseSettings


class Settings(BaseSettings):
    # Set sensible defaults; override via .env
    database_url: str = "sqlite:///./cmms.db"
    secret_key: str = "change-me-to-a-random-secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
