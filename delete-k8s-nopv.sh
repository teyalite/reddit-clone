#!/bin/bash
#Commands to delete k8s deployments and services of the project
kubectl delete deployment postgres-deployment api-deployment
kubectl delete service postgres-service api-service
