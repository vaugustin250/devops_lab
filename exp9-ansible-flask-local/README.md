# Experiment 9: Ansible Deploy Flask App Locally

## Objective
Use Ansible to deploy a Flask application locally using a Python virtual environment, Gunicorn WSGI server, and a `systemd` service (`http://127.0.0.1:8000`) with idempotency.

## Prerequisites (Linux / WSL with systemd enabled)
```bash
sudo apt update && sudo apt install -y ansible
```

## How to Run
```bash
# 1. Test connectivity
ansible -i inventory.ini all -m ping

# 2. Deploy
ansible-playbook playbook.yml -K

# 3. Verify
curl http://127.0.0.1:8000
systemctl status ansible-flask.service

# 4. Verify idempotency (run again)
ansible-playbook playbook.yml -K
```
