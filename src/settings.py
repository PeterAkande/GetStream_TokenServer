import os.path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    This would handle the whole settings for the application
    It would, for now, handle the app id an the primary certificate.

    Just make sure that a .env file exists in the base directory of the project
    """

    API_KEY: str
    API_SECRET: str

    class Config:
        env_file = os.path.join(os.getcwd(), ".env")


settings = Settings()
