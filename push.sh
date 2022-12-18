#!/bin/bash
# Commands to build and push docker image to docker hub
docker-compose build --no-cache
docker image tag reddit-clone-api teyalite/reddit-clone-api
docker push teyalite/reddit-clone-api
