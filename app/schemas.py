from pydantic import BaseModel
from datetime import datetime


class TokenData(BaseModel):
    sub: str


class Token(BaseModel):
    access_token: str
    token_type: str


# class UserCreate(BaseModel):
#     username: string
#     password: str


# class UserOut(BaseModel):
#     id: int
#     username: string
#     created_at: datetime

#     class Config:
#         orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str
