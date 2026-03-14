# Notes App (FastAPI + SQLAlchemy)

A simple Notes application with user authentication and CRUD functionality.  
Built using **FastAPI**, **SQLAlchemy**, and **Alembic**, this project contains secure login flows, database migrations, and  backend design.

---

## Features
- User signup & login with JWT authentication
- Create, read, update, and delete notes. 
- Cascade delete (removes the user and their notes)
- Alembic migrations for database schema management
- Modular project structure with routers for clean code organization

---

## Tech Stack
- **FastAPI** – Python web framework
- **SQLAlchemy** – ORM for database operations
- **Alembic** – database migrations
- **JWT (python-jose)** – token-based authentication
- **Passlib** – password hashing

---

## Setup

Clone the repository and set up the environment:

```bash
git clone https://github.com/abraham-ahmer/notes_app.git
cd notes_app
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
uvicorn main: app --reload


