# Whatsub Users Microservice (FastAPI)

A user microservice for a subscription management tool, implemented in Python with FastAPI.

## Structure

```
app/
  main.py
  middleware/
  models/
  resources/
  services/
  utils/
```

- middleware: Request logging and error handling
- models: Pydantic schemas for request/response
- resources: FastAPI routers/controllers
- services: Business logic and persistence adapters
- utils: Logger and settings utilities

## Getting Started (conda)

1. Create and activate a conda environment

```bash
conda create -n whatsub-users python=3.12 -y
conda activate whatsub-users
```

2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

3. Configure environment variables

```bash
cp .env.example .env
# edit .env as needed
```

4. Run the server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Alternative: module mode or direct file
```bash
python -m app.main
# or
python app/main.py
```

5. Open API docs

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Health Check

- GET /health → { "status": "ok" }

## Users API (in-memory)

- POST /users create user
- GET /users list users
- GET /users/{user_id} get user by id
- PATCH /users/{user_id} update user
- DELETE /users/{user_id} delete user

This service uses an in-memory store for demo purposes. Replace with a real repository in services/user_service.py when integrating with a database.
