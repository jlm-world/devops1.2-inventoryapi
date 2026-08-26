# Project 2 — Inventory API

A containerized REST API for inventory management, built with Flask and PostgreSQL, running inside Docker containers.

---

## Overview

This project demonstrates containerization of a full-stack application using Docker and Docker Compose. It includes a Flask API with full CRUD operations, a PostgreSQL database, persistent storage, and environment-based configuration.

---

## Tech Stack

- Python 3.10
- Flask
- PostgreSQL 16
- Docker
- Docker Compose
- Git & GitHub
- Docker Hub

---

## Architecture

The application consists of two services:

- **Flask API** — handles HTTP requests and business logic
- **PostgreSQL** — persistent data storage

Both services run in separate containers, connected via a Docker network. Database data is persisted using a named Docker volume.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | Retrieve all products |
| GET | `/products/<id>` | Retrieve a single product |
| POST | `/products` | Create a new product |
| PUT | `/products/<id>` | Update an existing product |
| DELETE | `/products/<id>` | Delete a product |

---

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone the repository:

```bash
git clone https://github.com/jlm-world/devops1.2-inventoryapi.git
cd devops1.2-inventoryapi
```

2. Create a `.env` file with the following variables:

```bash
POSTGRES_USER=inventory
POSTGRES_PASSWORD=inventorypass
POSTGRES_DB=inventory
```

3. Build and start the containers:

```bash
docker compose up --build -d
```

4. Verify the API is running:

```bash
curl http://localhost:5000/products
```

---

## Docker Hub

The image is publicly available:

```bash
mfraj1/inventory-api:latest
```

Link: [https://hub.docker.com/r/mfraj1/inventory-api](https://hub.docker.com/r/mfraj1/inventory-api)

---

## Project Status

✅ Complete — runs locally with `docker compose up --build`
# Trigger workflow
# Test auto-deploy
