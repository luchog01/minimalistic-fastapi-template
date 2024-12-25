# Hero API 🦸‍♂️
A modern, production-ready FastAPI template for building scalable APIs.

## Features ✨
- 🔄 Complete CRUD operations for heroes
- 📊 Async SQLAlchemy with PostgreSQL
- 🔄 Automatic Alembic migrations
- 🏗️ Clean architecture with repository pattern
- ⚠️ Custom exception handling
- 🔍 CI and testing pipeline
- 🧹 Linter setup with pre-commit hooks
- 🚂 One-click Railway deployment

## Deploy Now! 🚀
[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/template/wbTudS?referralCode=beBXJA)

## Project Structure 📁
```
api/
├── core/              # Core functionality
│   ├── config.py      # Environment and app configuration
│   ├── database.py    # Database connection and sessions
│   ├── exceptions.py  # Global exception handlers
│   ├── logging.py     # Logging configuration
│   └── security.py    # Authentication and security
├── src/
│   ├── heroes/        # Heroes module
│   │   ├── models.py      # Database models
│   │   ├── repository.py  # Data access layer
│   │   ├── routes.py      # API endpoints
│   │   └── schemas.py     # Pydantic models
│   └── users/         # Users module
│       ├── models.py      # User models
│       ├── repository.py  # User data access
│       ├── routes.py      # User endpoints
│       └── schemas.py     # User schemas
├── utils/            # Utility functions
└── main.py          # Application entry point
```

## Requirements 📋
- Python 3.8+
- PostgreSQL

## Setup 🛠️
1. Install uv (follow instructions [here](https://docs.astral.sh/uv/#getting-started))

2. Clone the repository:
```bash
git clone https://github.com/yourusername/minimalistic-fastapi-template.git
cd minimalistic-fastapi-template
```

3. Install dependencies with uv:
```bash
uv sync
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

5. Start the application:
```bash
uv run uvicorn app.main:app
```

## Creating a Migration 🔄
1. Make changes to your models
2. Generate migration:
```bash
alembic revision --autogenerate -m "your migration message"
```

Note: Migrations will be automatically applied when you start the application - no need to run `alembic upgrade head` manually!

## API Endpoints 📊
### Heroes
- `GET /heroes` - List all heroes
- `GET /heroes/{id}` - Get a specific hero
- `POST /heroes` - Create a new hero
- `PATCH /heroes/{id}` - Update a hero
- `DELETE /heroes/{id}` - Delete a hero

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get access token
- `GET /auth/me` - Get current user profile

## Example Usage 📝
Create a new hero:
```bash
curl -X POST "http://localhost:8000/heroes/" -H "Content-Type: application/json" -d '{
    "name": "Peter Parker",
    "alias": "Spider-Man",
    "powers": "Wall-crawling, super strength, spider-sense"
}'
```
