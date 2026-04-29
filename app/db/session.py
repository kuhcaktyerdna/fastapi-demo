from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm.session import Session

from app.config.settings import database_settings

POSTGRES_USER: str | None = database_settings.POSTGRES_USER
POSTGRES_PASSWORD: str | None = database_settings.POSTGRES_PASSWORD
POSTGRES_DB: str | None = database_settings.POSTGRES_DB
POSTGRES_URL: str | None = database_settings.POSTGRES_URL
DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}/{POSTGRES_DB}"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
