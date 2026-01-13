from sqlmodel import Session, select

from src.db import engine
from src.models import Permission


def seed_permissions(names: list[str]):
    with Session(engine) as session:
        for name in names:
            existing = session.exec(
                select(Permission).where(Permission.name == name)
            ).first()
            if not existing:
                perm = Permission(name=name)
                session.add(perm)
        session.commit()

def migrate_db():
    seed_permissions(["admin",])