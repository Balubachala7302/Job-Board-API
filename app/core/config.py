from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME:str="FastAPI Backend"
    DEBUG:bool=False

    SECRET_KEY: str="secret"
    ALGORITHM: str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int=30
    
    model_config = SettingsConfigDict(
        env_file=".env"
    )

@lru_cache
def get_settings():
    return Settings()