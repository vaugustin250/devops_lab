# Experiment 5: Reactive Web Page Using Jenkins and Docker

## Objective
Create and deploy a reactive JavaScript web page via a Jenkins pipeline running in Docker, publish it with HTML Publisher, and enable JavaScript execution via Jenkins CSP settings.

## How to Run
```bash
# 1. Start Jenkins
docker compose up -d

# 2. Allow JavaScript in Jenkins HTML Publisher
# Go to: Manage Jenkins > Script Console, and run:
#   System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")

# 3. Create Pipeline job 'karunya-reactive-site' using 'Jenkinsfile' and click Build Now.

# 4. Stop Jenkins when done
docker compose down
```
