# Flask Ansible Deployment Project

## Overview
This project demonstrates the CI/CD pipeline to deploy a Flask application using GitHub Actions and Ansible, including a SQLite database and unit tests.

## How to Run
1. Clone this repo.
2. Ensure the VM is running using Vagrant.
3. Push changes to GitHub to trigger the CD workflow.
4. Visit the app at: http://192.168.56.10:5000/

## Authors
Rohan Thapa and Team

## Directories
- `ansible/`: Contains playbook and inventory
- `.github/workflows/`: CI/CD config
- `templates/`: HTML templates
- `tests/`: Flask unit tests

## Secrets Required (GitHub Repository Settings)
- `VM_USERNAME` = `vagrant`
- `VM_IP` = `192.168.56.10`
- `VM_PRIVATE_KEY` = private SSH key content

## Notes
- Flask runs as a systemd service
- All files are deployed from GitHub push
- SQLite is used for message storage
- A test step is included in CI
test