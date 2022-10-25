from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, database, oauth2


router = APIRouter(prefix="/vote", tags=["Vote"])

# Up vote and down vote
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote_data: schemas.Vote,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
):

    post = (
        db.query(models.Post).filter(models.Post.id == vote_data.post_id).one_or_none()
    )

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post doesn't exist!"
        )

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote_data.post_id,
        models.Vote.user_id == current_user.id,
    )

    vote = vote_query.first()

    if vote_data.up_vote:
        if vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user has already voted on post{vote_data.post_id}",
            )
        vote = models.Vote(post_id=vote_data.post_id, user_id=current_user.id)

        db.add(vote)
        db.commit()

        return {"message": "Successfully added vote!"}

    if not vote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote doesn't exist!"
        )

    vote_query.delete(synchronize_session=False)
    db.commit()

    return {"message": "Successfully deleted vote!"}
