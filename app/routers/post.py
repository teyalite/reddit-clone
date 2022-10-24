from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, schemas, database, oauth2


router = APIRouter(prefix="/posts", tags=["Posts"])


# Get posts
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(database.get_db)):
    return (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .all()
    )


# Create a new post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(
    payload: schemas.PostCreate,
    db: Session = Depends(database.get_db),
    token_data: schemas.TokenData = Depends(oauth2.get_current_user),
):
    post = models.Post(owner_id=token_data.sub, **payload.dict())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post
