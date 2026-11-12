# Experiment 10: Ansible for Docker and Kubernetes

## Objective
Automate running an NGINX container on Docker and deploying NGINX onto a local `kind` Kubernetes cluster using Ansible playbooks.

## Prerequisites (Ubuntu / WSL)
```bash
sudo apt update && sudo apt install -y ansible
ansible-galaxy collection install -r requirements.yml
```

## How to Run
```bash
# 1. Run NGINX in Docker (port 8080)
ansible-playbook -i inventory.ini docker.yml -K
curl http://localhost:8080

# 2. Deploy NGINX on kind Kubernetes cluster
ansible-playbook -i inventory.ini k8s.yml -K
sudo kubectl port-forward svc/nginx 8081:80
# Open http://localhost:8081

# 3. Clean up
docker rm -f web
sudo kind delete cluster --name simple
```
