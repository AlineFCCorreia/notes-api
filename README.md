# 📝  Notes API - FastAPI

A simple Notes API built with FastAPI, allowing users to create, retrieve, update, and delete notes (Markdown supported).

## 🚀 Features

- Create, read, update, and delete notes.

- Automatic validation using Pydantic.

- Interactive API documentation with Swagger UI.

## 📞 Technologies Used

- FastAPI - High-performance API framework.

- Pydantic - Data validation and serialization.

- Uvicorn - ASGI server for running FastAPI.

## 💂️ Project Structure

```
api-notes/
│── main.py          # Entry point of the API
│── models.py        # Pydantic models for data validation
│── database.py      # Database setup (future enhancement)
│── routes/
│   ├── notes.py     # Notes-related API routes
│── pyproject.toml   # Poetry dependency management
```

## 🛠 Installation & Setup

1️⃣ Clone the repository

```
git clone https://github.com/AlineFCCorreia/api-notes.git
cd api-notes
```

2️⃣ Install dependencies using Poetry

```
poetry install
```

3️⃣ Run the application

```
poetry run uvicorn main:app --reload
```

4️⃣ Access the API

- Swagger UI: http://127.0.0.1:8000/docs

- ReDoc: http://127.0.0.1:8000/redoc

## 🛠 API Endpoints


| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | /notes | Retrieve all notes|
| GET | /notes/{id} | Get a single note |
| POST| /notes | Create a new note |
| PUT | /notes/{id} | Update a note |
| DELETE | /notes/{id} |Delete a note |

### 📌 Next Steps

- Implement a database (SQLite/PostgreSQL).

- Add Markdown rendering.

- Implement user authentication (JWT).

 
