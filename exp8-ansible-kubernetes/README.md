# Experiment 8: Ansible Integration with Kubernetes Cluster

## Objective
Configure Ansible with the `kubernetes.core` collection, connect to a Minikube cluster via kubeconfig, and automate cluster inspection and namespace creation.

## Prerequisites (Ubuntu / WSL)
```bash
sudo apt update && sudo apt install -y ansible python3-kubernetes
ansible-galaxy collection install kubernetes.core
minikube start --driver=docker
```

## How to Run
```bash
ansible-playbook test-k8s.yaml
ansible-playbook get-k8s-info.yaml
ansible-playbook create-namespace.yaml
kubectl get namespaces

# Clean up
kubectl delete namespace ansible-lab
```
