# Reddit Clone

Reddit Clone using fastapi

# Docker Image

The docker image for the project can be found here [teyalite/reddit-clone-api](https://hub.docker.com/r/teyalite/reddit-clone-api)

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

    -   Docker compose build without using the cache

        ```bash
        docker-compose build --no-cache
        ```

    -   Rename docker image

        ```bash
        docker image tag reddit-clone-api teyalite/reddit-clone-api
        ```

-   Kubernetes

    -   Start munikube

        ```bash
        minikube start
        ```

    -   Start k8s deployment and service for postgres

        ```bash
        kubectl apply -f postgres.yaml
        ```

    -   Start k8s deployment and service for the api

        ```bash
        kubectl apply -f api.yaml
        ```

    -   Minikube start the service tunnel

        ```bash
        minikube service api-service
        ```

    -   K8s delete deployment

        ```bash
        kubectl delete deployment deployment-name
        ```

    -   K8s interactive mode to execute command inside a container

        ```bash
        kubectl exec -it pod-name bash
        ```

# Heroku (Deployment and config files)

-   **_runtime.txt_** file contains the python version used for the application development. It'is used to specify a Python runtime for Heroku deployment
-   **_Procfile_** contains the command that are executed by the application on startup
