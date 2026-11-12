# Experiment 7: Kubernetes Deployment and Service for Python App

## Objective
Deploy a containerized Python Flask web application (`dockersamples/flaskapp:latest`) to Minikube with 2 replicas and expose it via a NodePort Service.

## How to Run
```bash
# 1. Ensure Minikube is running
minikube start --driver=docker
kubectl get nodes

# 2. Apply Deployment & Service
kubectl apply -f python-deployment.yaml
kubectl apply -f python-service.yaml

# 3. Verify & Access
kubectl get deployments
kubectl get pods
kubectl get svc
minikube service python-web-service --url

# 4. Clean up
kubectl delete svc python-web-service
kubectl delete deployment python-web-deployment
```
