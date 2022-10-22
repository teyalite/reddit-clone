from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .config import settings
from .routers import auth, user

# command to run the app: uvicorn app.main:app --reload
app = FastAPI()


app.include_router(auth.router)
app.include_router(user.router)


@app.get("/")
def index():
    print(settings)
    return "Hello world!!"
