# Project 2 — Containerized Inventory API

A Flask REST API connected to PostgreSQL and containerized with Docker Compose.

## Tech Stack

- Python
- Flask
- PostgreSQL 16
- Docker
- Docker Compose

## Architecture

Client → Flask API → PostgreSQL

PostgreSQL data is stored in a Docker named volume for persistence.

## Run Locally

```bash
docker compose up -d
# conflict demo from dev
