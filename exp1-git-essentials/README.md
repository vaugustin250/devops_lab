# Experiment 1: Git Essentials – Commit, Push, Merge, and Pull Requests

## Objective
Implement version control fundamentals using Git and GitHub: repository initialization, staging, committing, branching, pushing, Pull Requests, and merging.

## Files
- `ex.py` — Sample Python script printing register number (`URK23AI1048`).
- `ex1.py` — Secondary Python script for branch/merge workflow.

## How to Run
```bash
# Run scripts directly
python ex.py
python ex1.py

# Git workflow practice
git init
git status
git add .
git commit -m "initial commit"
git branch -M main
git checkout -b main1
git add .
git commit -m "feature update"
git checkout main
git merge main1
```
