from fastapi import FastAPI
from .config import settings
from .routers import auth, user, post, vote

# command to run the app: uvicorn app.main:app --reload
app = FastAPI()


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(vote.router)


@app.get("/")
def index():
    print(settings)
    return "Hello world!!"
