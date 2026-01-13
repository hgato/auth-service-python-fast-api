from src.schemas import UserCreate
from sqlmodel import select
from src import models, utils
from src.models import Permission
from src.constants import DEFAULT_USER_PERMISSIONS


def create_base_user(user_input: UserCreate, db):
    new_user = models.User(
        email=user_input.email,
        password_hash=utils.hash_password(user_input.password),
    )
    permissions = db.exec(
        select(Permission).where(Permission.name.in_(DEFAULT_USER_PERMISSIONS))
    ).all()
    new_user.permissions = permissions
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
