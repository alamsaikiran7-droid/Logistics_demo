from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Logistics Intelligence API"
    secret_key: str = "change-me"
    access_token_expire_minutes: int = 120
    database_url: str = "sqlite:///./logistics.db"
    openai_api_key: str | None = None
    use_mock_ai: bool = True

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
