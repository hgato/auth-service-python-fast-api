"""Application constants loaded from configuration."""
from src.config import permissions_config

DEFAULT_PERMISSIONS = permissions_config.get("default_permissions", ["admin", "user"])
DEFAULT_USER_PERMISSIONS = permissions_config.get("default_user_permissions", ["user"])
PERMISSION_DESCRIPTIONS = permissions_config.get("permission_descriptions", {})

