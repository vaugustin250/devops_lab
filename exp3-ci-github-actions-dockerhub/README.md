# Experiment 3: CI Pipeline for a Python App Using GitHub Actions and Docker Hub

## Objective
Create a Python application with `pytest` unit tests and a GitHub Actions workflow that runs tests, builds a Docker image, and pushes it to Docker Hub.

## Run Locally
```bash
pip install -r requirements.txt
python app.py
pytest -q
```

## Run with Docker
```bash
docker build -t python-ci-lab:local .
docker run --rm python-ci-lab:local
```

## Enable GitHub Actions CI
1. Add repository secrets under **Settings > Secrets and variables > Actions**:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
2. Copy `.github/workflows/ci-dockerhub.yml` to the root `.github/workflows/` if running in a standalone repository.
3. Push to `main` or push a release tag (`git tag v1.0.0 && git push origin v1.0.0`).
