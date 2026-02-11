import os
import yaml
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')
    ISSUER_NAME: str = os.getenv('ISSUER_NAME')


settings = Settings()


def load_permissions_config():
    """Load permissions configuration from YAML file."""
    config_path = Path(__file__).parent.parent / "permissions.yaml"

    # Fallback defaults if file doesn't exist
    default_config = {
        "default_permissions": ["admin", "user", "moderator"],
        "default_user_permissions": ["user"],
        "permission_descriptions": {}
    }

    if not config_path.exists():
        print(f"Warning: {config_path} not found. Using default permissions.")
        print("Copy permissions.yaml.example to permissions.yaml to customize.")
        return default_config

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            return config if config else default_config
    except Exception as e:
        print(f"Error loading permissions config: {e}")
        print("Using default permissions.")
        return default_config


permissions_config = load_permissions_config()