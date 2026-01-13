from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from src.db import Base, engine, get_session
from src import models, schemas, utils

from src.db import init_db
from src.db_utils import create_base_user

from src.schemas import UserOut

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application is starting up (lifespan)!")
    db = next(get_session())
    db.commit()
    init_db()
    yield
    print("Application is shutting down (lifespan)!")

app = FastAPI(title="Auth Service with JWT + Permissions", lifespan=lifespan)


@app.post("/register", response_model=schemas.UserOut)
def register_user(user_input: schemas.UserCreate, db: Session = Depends(get_session)):
    if db.query(models.User).filter(models.User.email == user_input.email).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    new_user = create_base_user(user_input, db)

    return UserOut(
        id=new_user.id,
        email=new_user.email,
        permissions=[p.name for p in new_user.permissions]
    )


@app.post("/token", response_model=schemas.TokenResponse)
def login(user: schemas.UserCreate, db: Session = Depends(get_session)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not utils.verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    user = UserOut(
        id=db_user.id,
        email=db_user.email,
        permissions=[p.name for p in db_user.permissions]
    )

    access_token = utils.create_access_token(user.model_dump())
    refresh_token = utils.create_refresh_token(user.model_dump())
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@app.post("/token/refresh", response_model=schemas.AccessTokenResponse)
def refresh_token(token: schemas.AccessTokenRefreshRequest):
    decoded = utils.decode_token(token.refresh_token)
    if not decoded:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    access_token = utils.create_access_token(decoded)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@app.get("/verify", response_model=schemas.UserOut)
def verify_token(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    decoded = utils.decode_token(token)
    if not decoded:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return decoded
