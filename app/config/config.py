import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    URL_API_WEATHER:str = os.getenv("URL_API_WEATHER")
    API_KEY_WEATHER:str = os.getenv("API_KEY_WEATHER")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", default="db")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", default="5432")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

settings = Settings()
