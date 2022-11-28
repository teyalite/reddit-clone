# Reddit Clone

Reddit Clone using fastapi

# Commands

-   Virtual environment
    -   Create virtual enviromnent
        ```bash
        virtualenv venv
        ```
    -   Activate virtual environment on MacOs/Linux
        ```bash
        source ./venv/bin/activate
        ```
    -   Install dependencies in requirements.txt
        ```bash
        pip install -r requirements.txt
        ```
-   Alembic

    -   Alembic Initialisation
        ```bash
        alembic init alembic
        ```
    -   Alembic Autogenerate Revision
        ```bash
        alembic revision --autogenerate -m "Message"
        ```
    -   Alembic upgrade to latest revision
        ```bash
        alembic upgrade head
        ```

-   Fastapi Application
    -   Run the Fastapi application with reload(The application reload when detect changes) for development environment
        ```bash
        uvicorn app.main:app --reload
        ```
    -   Run the Fastapi application
        ```bash
        uvicorn app.main:app
        ```
-   Docker
    -   Interactive mode to run commands inside the container
        ```bash
        docker exec -it container_name bash
        ```

# Heroku (Deployment and config files)

-   **_runtime.txt_** file contains the python version used for the application development. It'is used to specify a Python runtime for Heroku deployment
-   **_Procfile_** contains the command that are executed by the application on startup
