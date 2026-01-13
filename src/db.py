from sqlmodel import SQLModel, create_engine, Session, select
from src.config import settings
from sqlalchemy.orm import declarative_base

connection_url = f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
engine = create_engine(connection_url, echo=False)

Base = declarative_base()

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
