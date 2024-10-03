from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True

class ArtPieceBase(BaseModel):
    title: str
    description: str

class ArtPieceCreate(ArtPieceBase):
    tags: List[str]

class ArtPiece(ArtPieceBase):
    id: int
    image_path: str
    upload_date: str
    tags: List[Tag]
    author: User

    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    rendering_rating: int
    anatomy_rating: int
    composition_rating: int
    rendering_comment: Optional[str] = None
    anatomy_comment: Optional[str] = None
    composition_comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    art_piece_id: int
    user: User
    global_rating: float

    class Config:
        orm_mode = True