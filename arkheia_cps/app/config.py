from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ARKHEIA-CPS"
    environment: str = "production"

settings = Settings()
