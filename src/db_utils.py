from src.schemas import UserCreate
from sqlmodel import select
from src import models, utils
from src.models import Permission


def create_base_user(user_input: UserCreate, db):
    new_user = models.User(
        email=user_input.email,
        password_hash=utils.hash_password(user_input.password),
    )
    permission_names = ['admin']
    permissions = db.exec(
        select(Permission).where(Permission.name.in_(permission_names))
    ).all()
    new_user.permissions = permissions
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
