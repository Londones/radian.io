from .database import Base, engine
from . import models

# Create database tables
models.Base.metadata.create_all(bind=engine)