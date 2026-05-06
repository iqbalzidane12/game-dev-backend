# Mekan Games — FastAPI Backend

REST API backend for the [Mekan Games](https://github.com/XusniddinQalandarov/game-dev-front) Angular frontend.

## Tech Stack

- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **SQLite** — database (dev)
- **JWT** — authentication via `python-jose`
- **passlib/bcrypt** — password hashing

## Project Structure

```
game-dev-backend/
├── main.py               # App entry point
├── seed.py               # DB seeder (games + admin user)
├── requirements.txt
├── .env.example
└── app/
    ├── config.py         # Settings (pydantic-settings)
    ├── database.py       # SQLAlchemy engine + session
    ├── models/
    │   ├── user.py       # User table
    │   └── game.py       # Game table
    ├── schemas/
    │   ├── auth.py       # Login / Register / Token
    │   ├── user.py       # UserResponse
    │   └── game.py       # GameResponse / GameCreate
    ├── routers/
    │   ├── auth.py       # /auth/register, /auth/login, /auth/me
    │   └── games.py      # /games, /games/search, /games/{id}
    └── core/
        ├── security.py   # JWT + bcrypt helpers
        └── deps.py       # get_current_user dependency
```

## API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/auth/register` | — | Create account → JWT |
| POST | `/auth/login` | — | Login → JWT |
| GET | `/auth/me` | ✓ | Current user info |
| GET | `/games` | ✓ | List all games |
| GET | `/games/search?q=` | ✓ | Search by title or genre |
| GET | `/games/{id}` | ✓ | Single game |

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Copy env file
cp .env.example .env

# 3. Seed the database
python seed.py

# 4. Run the server
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`

## Default Credentials (after seeding)

| Email | Password |
|-------|----------|
| admin@mekangames.com | password123 |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SECRET_KEY` | `changeme-...` | JWT signing key — **change in production** |
| `DATABASE_URL` | `sqlite:///./game_dev.db` | SQLAlchemy DB URL |
| `CORS_ORIGINS` | `["http://localhost:4200"]` | Allowed origins |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `1440` | Token lifetime (24 h) |
