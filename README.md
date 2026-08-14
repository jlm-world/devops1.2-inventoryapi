# Project 2 — Containerized Inventory API

A containerized Flask REST API for managing inventory, backed by PostgreSQL.

## Tech Stack

- Python
- Flask
- PostgreSQL 16
- Docker
- Docker Compose
- Git & GitHub
- Docker Hub

## Architecture

```text
Client
  |
  v
Flask Inventory API
  |
  | Docker Network
  v
PostgreSQL
  |
  v
Persistent Docker Volume
# Auto-deploy test
# Test workflow
# Fix SSH key
