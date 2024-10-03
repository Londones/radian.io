from .database_factory import db_factory, get_db

engine = db_factory.create_engine()
Base = db_factory.get_base()