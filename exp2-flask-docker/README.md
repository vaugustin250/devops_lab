# Experiment 2: Flask App Containerization and Docker Hub Deployment

## Objective
Design a Python Flask web application, containerize it using Docker, verify it locally, and push the image to Docker Hub.

## Run Locally (Without Docker)
```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

## Run with Docker
```bash
# 1. Build the Docker image
docker build -t flask-docker-app .

# 2. Run the container
docker run -d --name flask-app -p 5000:5000 flask-docker-app

# 3. Verify in browser
# Open http://localhost:5000

# 4. Push to Docker Hub (replace <dockerhub_user> with your username)
docker login
docker tag flask-docker-app <dockerhub_user>/flask-docker-app:latest
docker push <dockerhub_user>/flask-docker-app:latest

# 5. Clean up
docker stop flask-app && docker rm flask-app
```
