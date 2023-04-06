from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:12345@localhost:5433/qqq"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()


def get_db():
    db = SessionLocal
    try:
        yield db
    except:
        db.close_all()