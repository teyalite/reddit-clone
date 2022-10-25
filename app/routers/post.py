from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
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


# Retrieve a post
@router.get("/{id}", response_model=schemas.PostOut)
def retrieve_post(id: int, db: Session = Depends(database.get_db)):
    post = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.id == id)
        .one_or_none()
    )

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} not found"
        )
    return post


# Create a new post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(
    payload: schemas.PostCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
):
    post = models.Post(owner_id=current_user.id, **payload.dict())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post


# Delete a post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def retrieve_post(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} not found"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    post_query.delete(synchronize_session=False)
    db.commit()


# Update a post
@router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(
    id: int,
    payload: schemas.PostUpdate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} not found"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    post_query.update(payload.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()
