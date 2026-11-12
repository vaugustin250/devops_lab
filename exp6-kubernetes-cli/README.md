# Experiment 6: Manage Kubernetes Resources Using CLI

## Objective
Start a local Minikube Kubernetes cluster and manage Pods, Deployments, scaling, rolling updates, rollbacks, and NodePort Services using `kubectl`.

## How to Run
```bash
# 1. Start Minikube
minikube start --driver=docker
kubectl get nodes

# 2. Deploy and test Pod
kubectl apply -f nginx-pod.yaml
kubectl get pods
kubectl port-forward pod/nginx-pod 8080:80
# Open http://localhost:8080, then Ctrl+C and delete:
kubectl delete pod nginx-pod

# 3. Deployment, Scaling, Rolling Update & Rollback
kubectl create deployment my-nginx --image=nginx
kubectl scale deployment my-nginx --replicas=3
kubectl set image deployment/my-nginx nginx=nginx:1.25
kubectl rollout status deployment/my-nginx
kubectl rollout undo deployment/my-nginx

# 4. Expose as NodePort Service
kubectl expose deployment my-nginx --type=NodePort --port=80
minikube service my-nginx --url

# 5. Clean up
kubectl delete svc my-nginx
kubectl delete deployment my-nginx
```
