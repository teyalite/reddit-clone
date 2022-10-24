from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import models

from .config import settings
from .schemas import TokenData
from .database import get_db

oauth_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Get the token data, create access token then return the access token
def create_access_token(data: TokenData):
    to_encode = data.dict()

    to_encode.update(
        {
            "exp": datetime.utcnow()
            + timedelta(minutes=settings.jwt_access_token_expire_minutes)
        }
    )

    return jwt.encode(
        to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm
    )


# Verify the access token, and return the token data it contains if it's valid
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(
            token, settings.jwt_secret_key, algorithms=settings.jwt_algorithm
        )
        return TokenData(sub=payload.get("sub"))
    except JWTError as e:
        print(e, "JWTError")
        raise credentials_exception


def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Couldn't validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data: TokenData = verify_access_token(token, credentials_exception)

    return db.query(models.User).filter(models.User.id == token_data.sub).first()
