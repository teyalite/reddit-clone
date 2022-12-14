from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models, schemas, utils, database

router = APIRouter(prefix="/users", tags=["Users"])

# Create a new user
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(payload: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Hash the password
    payload.password = utils.hash(payload.password)
    user = models.User(**payload.dict())

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken, please try another one",
        )

    return user


# Get a single user
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id={id} doesn' exists",
        )

    return user
