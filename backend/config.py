from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_user:str
    db_password:str
    secret_key:str
    algorithm:str
    expire_after_days:int

    class Config:
        env_file = ".env"

settings = Settings()