from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship, Column, JSON

class UserPermissionLink(SQLModel, table=True):
    __tablename__ = "user_permission_links"
    user_id: int = Field(foreign_key="users.id", primary_key=True)
    permission_id: int = Field(foreign_key="permissions.id", primary_key=True)


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    password_hash: str
    is_active: bool = True

    permissions: List["Permission"] = Relationship(
        back_populates="users",
        link_model=UserPermissionLink
    )


class Permission(SQLModel, table=True):
    __tablename__ = "permissions"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)

    users: List[User] = Relationship(
        back_populates="permissions",
        link_model=UserPermissionLink
    )
