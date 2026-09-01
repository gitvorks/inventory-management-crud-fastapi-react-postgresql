# FastAPI Learning Project (inventory-management-crud-fastapi-react-postgresql)

Hands-on FastAPI implementation project, built while learning core backend/API concepts — path & query parameters, request/response models, validation, and (eventually) database-backed CRUD.

## Table of Contents

- [Overview & Purpose](#overview--purpose)
- [Tech Stack & Tools](#tech-stack--tools)
- [Project Methodology](#project-methodology)
- [API Docs & Screenshots](#api-docs--screenshots)
- [How to Run](#how-to-run)
- [Results & Future Work](#results--future-work)
- [Author & Contact](#author--contact)

## Overview & Purpose

This repository documents my hands-on journey learning **FastAPI**, a modern Python web framework for building APIs. Rather than just watching tutorials, each concept here is implemented, tested, and committed individually, so this repo doubles as both a **learning log** and a **working demonstration** of REST API fundamentals — request/response cycles, HTTP methods, data validation, and (as the project grows) persistence with a real database.

The goal: be able to design, build, and reason about the trade-offs in a production-style backend API, not just copy working code.

## Tech Stack & Tools

- **Language:** Python 3.x
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Server:** Uvicorn (ASGI server)
- **Data validation:** Pydantic
- **Version control:** Git & GitHub
- _(Will expand as the project grows — e.g. SQLAlchemy, a database, Docker, testing tools)_

## API Docs & Screenshots

FastAPI auto-generates interactive API documentation from the code's type hints, available at `/docs` (Swagger UI) when the app is running.

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/gitvorks/inventory-management-crud-fastapi-react-postgresql.git
cd fastapi-learning

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn main:app --reload

# 5. Open in browser
# App:  http://127.0.0.1:8000
# Docs: http://127.0.0.1:8000/docs
```

## Results & Future Work

**Current state:** Basic routing and path parameters implemented and working.

**Planned next steps:**

- [ ] Query parameters with validation and default values
- [ ] Pydantic models for request bodies (POST/PUT endpoints)
- [ ] Database integration with SQLAlchemy
- [ ] Full CRUD API for a real resource (e.g. a simple task/user management API)
- [ ] Dependency injection for shared logic (auth, DB sessions)
- [ ] Basic tests with pytest
- [ ] Deployment (e.g. Render/Railway/Docker)

## Author & Contact

**Ansh Verma**
📧 [anshvorks1906@example.com]
💼 [https://www.linkedin.com/in/anshvorks1906/]
🐙 [https://github.com/gitvorks]
