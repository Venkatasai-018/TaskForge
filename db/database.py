from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base


SQL_URL='postgresql://postgres:12345@localhost/postgres'

engine=create_engine(SQL_URL)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print("DB dependency error:", e)  # log it
        raise  # MUST re-raise
    finally:
        db.close()