from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, models, database, utils, oauth2

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Login path that returns the access token
@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = (
        db.query(models.User).filter(models.User.username == form_data.username).first()
    )

    if not user or not utils.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User with this username not found"
            if not user
            else "Incorrect password",
        )

    print(user.id)

    return {
        "access_token": oauth2.create_access_token(
            data=schemas.TokenData(sub=str(user.id))
        ),
        "token_type": "bearer",
    }
