# kubernetes-rbac-risk
Kubernetes RBAC risk course project exercise repository

## Overview
This project demonstrates how a Kubernetes deployment can appear healthy while still exposing a secret, granting excessive permissions, and leaking sensitive information through the application itself.

## Contents
- `app.py` - vulnerable Flask application used for the lab exercise
- `Dockerfile` - container image definition
- `requirements.txt` - Python dependencies
- `deployment-bad.yaml` - insecure Kubernetes deployment
- `service-bad.yaml` - publicly exposed service
- `rbac-bad.yaml` - cluster-admin binding for CI/CD
- `secret.yaml` - secure Secret-based configuration
- `deployment-fixed.yaml` - corrected deployment using a Secret
- `rbac-fixed.yaml` - least-privilege RBAC

## Status
Status: in progress
