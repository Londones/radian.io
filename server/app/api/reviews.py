from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, auth
from ..database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.Review, status_code=status.HTTP_201_CREATED)
def create_review(
    review: schemas.ReviewCreate,
    art_piece_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    """
    Create a new review for an art piece.

    - **review**: The review details including ratings and optional comments
    - **art_piece_id**: The ID of the art piece being reviewed

    Returns the created review.
    """
    return crud.create_review(db, review=review, art_piece_id=art_piece_id, user_id=current_user.id)

@router.get("/{art_piece_id}", response_model=List[schemas.Review])
def read_reviews(
    art_piece_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve all reviews for a specific art piece.

    - **art_piece_id**: The ID of the art piece to get reviews for

    Returns a list of reviews for the specified art piece.
    """
    return crud.get_reviews(db, art_piece_id=art_piece_id)