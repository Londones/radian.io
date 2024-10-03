from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash
from datetime import datetime
from typing import List

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_or_create_tag(db: Session, tag_name: str):
    tag = db.query(models.Tag).filter(models.Tag.name == tag_name).first()
    if not tag:
        tag = models.Tag(name=tag_name)
        db.add(tag)
        db.commit()
        db.refresh(tag)
    return tag

def create_art_piece(db: Session, art_piece: schemas.ArtPieceCreate, user_id: int, image_path: str):
    db_art_piece = models.ArtPiece(
        title=art_piece.title,
        description=art_piece.description,
        author_id=user_id,
        image_path=image_path,
        upload_date=datetime.now().isoformat()
    )
    for tag_name in art_piece.tags:
        tag = get_or_create_tag(db, tag_name)
        db_art_piece.tags.append(tag)
    db.add(db_art_piece)
    db.commit()
    db.refresh(db_art_piece)
    return db_art_piece

def get_art_pieces(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.ArtPiece).order_by(models.ArtPiece.upload_date.desc()).offset(skip).limit(limit).all()

def get_art_piece(db: Session, art_piece_id: int):
    return db.query(models.ArtPiece).filter(models.ArtPiece.id == art_piece_id).first()

def create_review(db: Session, review: schemas.ReviewCreate, art_piece_id: int, user_id: int):
    db_review = models.Review(**review.dict(), art_piece_id=art_piece_id, user_id=user_id)
    db_review.global_rating = (review.rendering_rating + review.anatomy_rating + review.composition_rating) / 3
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session, art_piece_id: int):
    return db.query(models.Review).filter(models.Review.art_piece_id == art_piece_id).all()

def search_art_pieces(db: Session, query: str):
    return db.query(models.ArtPiece).join(models.ArtPiece.tags).filter(
        (models.ArtPiece.title.ilike(f"%{query}%")) |
        (models.ArtPiece.description.ilike(f"%{query}%")) |
        (models.User.username.ilike(f"%{query}%")) |
        (models.Tag.name.ilike(f"%{query}%"))
    ).distinct().all()

def get_tags(db: Session):
    return db.query(models.Tag).all()