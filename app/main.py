from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .config import settings

# command to run the app: $uvicorn app.main:app --reload
app = FastAPI()


@app.get("/")
def index():
    print(settings)
    return "Hello world!!"
