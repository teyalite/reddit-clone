from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .config import settings
from .routers import auth

# command to run the app: uvicorn app.main:app --reload
app = FastAPI()


app.include_router(auth.router)


@app.get("/")
def index():
    print(settings)
    return "Hello world!!"
