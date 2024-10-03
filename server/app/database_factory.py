from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseFactory:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.engine = None
        self.SessionLocal = None
        self.Base = declarative_base()

    def create_engine(self):
        if not self.engine:
            self.engine = create_engine(self.database_url)
        return self.engine

    def create_session(self):
        if not self.SessionLocal:
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.create_engine())
        return self.SessionLocal()

    def get_base(self):
        return self.Base

db_factory = DatabaseFactory()

def get_db():
    db = db_factory.create_session()
    try:
        yield db
    finally:
        db.close()