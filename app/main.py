from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .routers import auth, user, post, vote
from .config import settings

# command to run the app: uvicorn app.main:app --reload
app = FastAPI()


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(vote.router)


@app.get("/", response_class=HTMLResponse)
def index():
    print(settings)

    return """
    <html>
        <head>
            <title>Reddit Clone Api by teyalite</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <style>
            html {
                width: 100%;
                height: 100%;
                display: flex;
            }
            
            body {
                text-align: center;
                flex: 1;
                display: flex;
                align-items: center;
                flex-direction: column;
                justify-content: center;
            }
            a {
                text-decoration: none;
            }
        </style>
        <body>
            <h1>Hi, this api was built by <a href='https://github.com/teyalite'>Abdoulkader Haidara</a></h1>
            <h2><a href='https://github.com/teyalite/reddit-clone'>Source code</a></h2>
        </body>
    </html>
    """
