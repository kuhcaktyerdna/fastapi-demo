import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
POSTGRES_USER: str | None = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str | None = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB: str | None = os.getenv("POSTGRES_DB")
POSTGRES_URL: str | None = os.getenv("POSTGRES_HOST", "localhost:5432")
DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}/{POSTGRES_DB}"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()