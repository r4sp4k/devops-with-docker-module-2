# Docker Demo: Click Counter

A minimal sample project for the 2_11 docker exercise. A tiny web app with one button that saves every click to a PostgreSQL database, with both services running in Docker via docker-compose.

## Components

| File | Purpose |
|---|---|
| `app.py` | Flask web application. Serves the page, handles the click endpoint, and writes to Postgres. |
| `templates/index.html` | The UI: one button and the current click count, updated via JavaScript. |
| `Dockerfile` | Builds the web app image (Python 3.12 + Flask + psycopg). |
| `requirements.txt` | Python dependencies (`flask`, `psycopg[binary]`). |
| `docker-compose.yaml` | Defines and wires the two services. |

## Services

- **web** — the Flask app, built from the local Dockerfile.
- **db** — official `postgres:16-alpine` image, data persisted in a named volume (`pgdata`).

The app reaches the database at hostname `db` (the compose service name) using the `DATABASE_URL` environment variable. On startup it creates the `clicks` table if it does not exist.

## Running

```bash
docker compose up --build
```

Then open **http://localhost:5000** and click the button. Each click inserts a row into the database and the counter updates.

## Ports

| Service | Host port | Container port |
|---|---|---|
| web (Flask) | **5000** | 5000 |
| db (Postgres) | not exposed | 5432 |

Postgres is only reachable inside the compose network, which is intentional; nothing else needs to talk to it.

## Stopping and resetting

```bash
docker compose stop          # stop, keep data
docker compose down          # stop and remove containers (volume keeps data)
docker compose down -v       # also wipe the database volume
```