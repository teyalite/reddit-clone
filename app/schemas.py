from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr


class TokenData(BaseModel):
    sub: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    username: constr(min_length=1, strip_whitespace=True)
    password: constr(min_length=4, max_length=70)
    bio: Optional[str] = None


class UserOut(BaseModel):
    id: int
    username: str
    created_at: datetime
    bio: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str


class PostBase(BaseModel):
    title: constr(min_length=1, strip_whitespace=True)
    content: constr(min_length=1, strip_whitespace=True)


class Post(PostBase):
    id: int
    created_at: datetime
    published: bool
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    published: bool = True


class PostOut(BaseModel):
    Post: Post
    votes: int
