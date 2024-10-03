from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from typing import List

router = APIRouter()

@router.get("/", response_model=List[schemas.Tag])
def read_tags(db: Session = Depends(get_db)):
    """
    Retrieve all tags.

    Returns a list of all tags in the system.
    """
    return crud.get_tags(db)