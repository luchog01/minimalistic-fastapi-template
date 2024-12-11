# Hero API

A FastAPI-based CRUD application for managing heroes, following best practices and modern Python async patterns.

## Features

- Full CRUD operations for heroes
- Async SQLAlchemy with PostgreSQL
- Alembic migrations
- Clean architecture with repository pattern
- Custom exception handling
- Type hints and documentation

## Project Structure

```
app/
├── core/
│   ├── config.py      # Application configuration
│   └── database.py    # Database setup and session management
├── heroes/
│   ├── exceptions.py  # Custom exceptions
│   ├── models.py      # SQLAlchemy models
│   ├── repository.py  # Database operations
│   ├── routes.py      # API endpoints
│   ├── schemas.py     # Pydantic models
│   └── service.py     # Business logic
└── main.py           # FastAPI application setup
```

## Requirements

- Python 3.8+
- PostgreSQL
- Dependencies listed in requirements.txt

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create PostgreSQL database:
```sql
CREATE DATABASE hero_db;
```

4. Set up environment variables (or create .env file):
```
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/hero_db
```

5. Run database migrations:
```bash
alembic upgrade head
```

6. Start the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /heroes` - List all heroes
- `GET /heroes/{id}` - Get a specific hero
- `POST /heroes` - Create a new hero
- `PATCH /heroes/{id}` - Update a hero
- `DELETE /heroes/{id}` - Delete a hero

## Example Usage

Create a new hero:
```bash
curl -X POST "http://localhost:8000/heroes/" -H "Content-Type: application/json" -d '{
    "name": "Peter Parker",
    "alias": "Spider-Man",
    "powers": "Wall-crawling, super strength, spider-sense"
}'
```

## Development

To create a new database migration:
```bash
alembic revision --autogenerate -m "description"
```

To apply migrations:
```bash
alembic upgrade head
```
