# release_tracker

FastAPI service for tracking software project releases.

## Stack

- FastAPI + SQLModel
- PostgreSQL via psycopg
- Alembic migrations
- Docker Compose for local run

## Quick start

```bash
uv sync
docker compose up -d
uv run alembic upgrade head
uv run fastapi dev
```
