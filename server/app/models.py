from sqlalchemy import Column, Integer, String, Text, Float, Table, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

art_tags = Table('art_tags', Base.metadata,
    Column('art_id', Integer, ForeignKey('art_pieces.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    art_pieces = relationship("ArtPiece", back_populates="author")
    reviews = relationship("Review", back_populates="user")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class ArtPiece(Base):
    __tablename__ = "art_pieces"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    image_path = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    upload_date = Column(String)
    tags = relationship("Tag", secondary=art_tags, backref="art_pieces")
    reviews = relationship("Review", back_populates="art_piece")
    author = relationship("User", back_populates="art_pieces")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    art_piece_id = Column(Integer, ForeignKey("art_pieces.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rendering_rating = Column(Integer)
    anatomy_rating = Column(Integer)
    composition_rating = Column(Integer)
    rendering_comment = Column(Text, nullable=True)
    anatomy_comment = Column(Text, nullable=True)
    composition_comment = Column(Text, nullable=True)
    global_rating = Column(Float)
    art_piece = relationship("ArtPiece", back_populates="reviews")
    user = relationship("User", back_populates="reviews")