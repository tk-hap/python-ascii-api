from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ASCII API"
    db_host: str
    db_port: int


settings = Settings()
