from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, status
from sqlalchemy.orm import Session
from .. import crud, schemas, auth
from ..database import get_db
import shutil
import os
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.ArtPiece)
async def create_art_piece(
    title: str,
    description: str,
    tags: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    """
    Create a new art piece.

    - **title**: The title of the art piece
    - **description**: A description of the art piece
    - **tags**: Comma-separated list of tags
    - **file**: The image file of the art piece

    Returns the created art piece.
    """
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    
    tag_list = [tag.strip() for tag in tags.split(',')]
    art_piece = schemas.ArtPieceCreate(title=title, description=description, tags=tag_list)
    return crud.create_art_piece(db, art_piece, current_user.id, file_location)

@router.get("/", response_model=List[schemas.ArtPiece])
def read_art_pieces(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """
    Retrieve a list of art pieces.

    - **skip**: Number of art pieces to skip (for pagination)
    - **limit**: Maximum number of art pieces to return

    Returns a list of art pieces.
    """
    return crud.get_art_pieces(db, skip=skip, limit=limit)

@router.get("/{art_piece_id}", response_model=schemas.ArtPiece)
def read_art_piece(art_piece_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific art piece by ID.

    - **art_piece_id**: The ID of the art piece to retrieve

    Returns the requested art piece or 404 if not found.
    """
    art_piece = crud.get_art_piece(db, art_piece_id=art_piece_id)
    if art_piece is None:
        raise HTTPException(status_code=404, detail="Art piece not found")
    return art_piece

@router.get("/search/", response_model=List[schemas.ArtPiece])
def search_art_pieces(q: str, db: Session = Depends(get_db)):
    """
    Search for art pieces.

    - **q**: Search query string

    Returns a list of art pieces matching the search query.
    """
    return crud.search_art_pieces(db, query=q)