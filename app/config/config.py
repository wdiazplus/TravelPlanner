import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    URL_API_WEATHER:str = os.getenv("URL_API_WEATHER")
    API_KEY_WEATHER:str = os.getenv("API_KEY_WEATHER")

settings = Settings()
