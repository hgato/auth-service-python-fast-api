from pydantic import BaseModel
from typing import List, Optional


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class AccessTokenRefreshRequest(BaseModel):
    refresh_token: str

class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    password: str
    roles: Optional[List[str]] = []
    permissions: Optional[List[str]] = []


class TokenPayload(BaseModel):
    sub: str
    roles: List[str] = []
    permissions: List[str] = []
    perm_version: int = 0
    exp: int


class UserOut(BaseModel):
    id: int
    email: str
    permissions: List[str]

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    password: str