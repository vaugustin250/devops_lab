# Experiment 4: Jenkins Deployment Using Docker

## Objective
Run Jenkins inside Docker using Docker Compose, create a Pipeline job that generates a static HTML/CSS site, publish it with HTML Publisher, and archive the build artifacts.

## How to Run
```bash
# 1. Start Jenkins
docker compose up -d

# 2. Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# 3. Open http://localhost:8080 in your browser
#    - Install suggested plugins
#    - Install 'HTML Publisher' plugin (Manage Jenkins > Plugins)
#    - Create a New Item -> Pipeline -> paste contents of 'Jenkinsfile' -> Build Now

# 4. Stop Jenkins when done
docker compose down
```
