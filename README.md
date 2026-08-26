# Project 2 — Inventory API

A containerized Flask REST API for managing inventory, backed by PostgreSQL.

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

text

---

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- Inventory management (products with name, price, quantity)
- Containerized with Docker
- Persistent database volume
- Environment variable configuration

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | List all products |
| GET | `/products/<id>` | Get a single product |
| POST | `/products` | Add a new product |
| PUT | `/products/<id>` | Update a product |
| DELETE | `/products/<id>` | Delete a product |

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jlm-world/devops1.2-inventoryapi.git
cd devops1.2-inventoryapi
2. Create a .env file
bash
POSTGRES_USER=inventory
POSTGRES_PASSWORD=inventorypass
POSTGRES_DB=inventory
3. Build and run with Docker Compose
bash
docker compose up --build -d
4. Test the API
bash
curl http://localhost:5000/products
Docker Hub
Image: mfraj1/inventory-api:latest

Project Status
✅ Complete — working locally with docker compose up --build

text

---

## Step 5 — Click **"Commit changes"**

Write a commit message like:
Update README with clean structure and API docs

text

Click **"Commit directly to the main branch"**

---

**Done, Raj.** 😎


