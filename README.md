# 24CS2019 DevOps Laboratory

Complete, ready-to-run collection of all **10 DevOps Lab Experiments** (`24CS2019`), organized by experiment with verified configurations, Dockerfiles, CI/CD pipelines, Kubernetes manifests, and Ansible playbooks.

- **Name:** V Augustin Prabakar
- **Register No:** `URK23AI1048`
- **Repository:** [vaugustin250/devops_lab](https://github.com/vaugustin250/devops_lab)

---

## Experiments Index

| Exp No | Experiment Title | Folder | Key Technologies |
| :---: | :--- | :--- | :--- |
| **1** | Git Essentials – Commit, Push, Merge, and Pull Requests | [`exp1-git-essentials/`](./exp1-git-essentials) | Git, GitHub, Python |
| **2** | Flask App Containerization and Docker Hub Deployment | [`exp2-flask-docker/`](./exp2-flask-docker) | Python, Flask, Docker, Docker Hub |
| **3** | CI Pipeline for a Python App Using GitHub Actions and Docker Hub | [`exp3-ci-github-actions-dockerhub/`](./exp3-ci-github-actions-dockerhub) | Python, pytest, GitHub Actions, Docker |
| **4** | Jenkins Deployment Using Docker | [`exp4-jenkins-docker/`](./exp4-jenkins-docker) | Docker Compose, Jenkins, HTML Publisher |
| **5** | Reactive Web Page Using Jenkins and Docker | [`exp5-jenkins-reactive-webapp/`](./exp5-jenkins-reactive-webapp) | Docker Compose, Jenkins, HTML/CSS/JS |
| **6** | Manage Kubernetes Resources Using CLI | [`exp6-kubernetes-cli/`](./exp6-kubernetes-cli) | Docker, kubectl, Minikube |
| **7** | Kubernetes Deployment and Service for Python App | [`exp7-k8s-python-app/`](./exp7-k8s-python-app) | Kubernetes, Minikube, NodePort |
| **8** | Ansible Integration with Kubernetes Cluster | [`exp8-ansible-kubernetes/`](./exp8-ansible-kubernetes) | Ansible, `kubernetes.core`, Minikube |
| **9** | Ansible Deploy Flask App Locally | [`exp9-ansible-flask-local/`](./exp9-ansible-flask-local) | Ansible, Flask, Gunicorn, systemd |
| **10** | Ansible for Docker and Kubernetes | [`exp10-ansible-docker-k8s/`](./exp10-ansible-docker-k8s) | Ansible, Docker, kind, Kubernetes |

---

## Quick Start (Run Anywhere)

1. **Clone this repository:**
   ```bash
   git clone https://github.com/vaugustin250/devops_lab.git
   cd devops_lab
   ```
2. **Navigate to any experiment folder** (e.g., `cd exp2-flask-docker`) and follow the step-by-step instructions in that folder's `README.md`.

---

## Prerequisites by Environment

- **Exp 1:** Git, Python 3.x
- **Exp 2–5:** Docker Desktop / Docker Engine + Docker Compose
- **Exp 6–7:** Docker + `kubectl` + Minikube
- **Exp 8–10:** Ubuntu / WSL2 (Linux) with Ansible (`ansible-core >= 2.15`)
