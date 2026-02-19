# Task Manager Application

A full-stack Task Management System built using:

- Django (Backend API)
- Django REST Framework
- django-filter
- Typer (CLI Interface)
- Bootstrap (Frontend UI)
- SQLite (Database)

This project provides:
- RESTful API
- Command Line Interface (CLI)
- Web Frontend Interface

---

#  Features

##  Backend (Django REST API)
- Create, Read, Update, Delete tasks
- Mark tasks as complete/incomplete
- Filter tasks by:
  - Status (pending/completed)
  - Priority (low/medium/high)
  - Due date range
- Validation:
  - Title cannot be empty
  - Due date cannot be in the past
- Persistent SQLite database

##  CLI Interface
- Create tasks
- List tasks
- Filter tasks
- Mark complete
- Delete tasks

##  Frontend (Bootstrap UI)
- Beautiful responsive UI
- Add task
- Delete task
- Toggle status
- Filter tasks
- Styled with Bootstrap 5

---

#  Project Structure

```
task_manager/
│
├── backend/
│   ├── manage.py
│   ├── config/
│   └── tasks/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── filters.py
│       ├── urls.py
│
├── cli/
│   └── cli.py
│
├── frontend/
│   ├── index.html
│   └── script.js
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️ Clone Project

```
git clone https://github.com/HemishPansuriya/task-manager.git
cd task_manager
```

---

## 2️ Create Virtual Environment

### Windows
```
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux
```
python3.12 -m venv venv
source venv/bin/activate
```

---

## 3️ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️ Run Database Migrations

```
cd backend
python manage.py migrate
```

---

## 5️ Start Backend Server

```
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/tasks
```

---

#  API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /tasks/ | List all tasks |
| POST | /tasks/ | Create task |
| GET | /tasks/{id}/ | Retrieve task |
| PUT | /tasks/{id}/ | Update task |
| PATCH | /tasks/{id}/ | Partial update |
| DELETE | /tasks/{id}/ | Delete task |
| POST | /tasks/{id}/mark_complete/ | Mark complete |
| POST | /tasks/{id}/mark_incomplete/ | Mark incomplete |

---

#  Filtering Examples

```
/tasks/?status=pending
/tasks/?priority=high
/tasks/?due_before=2026-12-31T00:00:00
/tasks/?due_after=2026-01-01T00:00:00
```

---

# CLI Usage

Make sure backend server is running.

Go to project root:

```
python cli/cli.py create "Buy Milk" --priority high
python cli/cli.py list
python cli/cli.py complete 1
python cli/cli.py delete 1
```

Optional filters:

```
python cli/cli.py list --status pending
python cli/cli.py list --priority high
```

---

# Frontend Usage

1. Start backend server
2. Open:

```
frontend/index.html or http://127.0.0.1:5500/frontend/index.html
```

Features:
- Add new task
- Delete task
- Toggle completion
- Filter tasks
- Responsive Bootstrap UI

---

# Database

- Default: SQLite
- File automatically created in backend directory
- Data persists between restarts

---

#  Assumptions

- Single-user application
- No authentication required
- Backend runs locally
- Frontend connects to local API



# Requirements

annotated-doc==0.0.4
asgiref==3.11.1
certifi==2026.1.4
charset-normalizer==3.4.4
click==8.3.1
colorama==0.4.6
Django==6.0.2
django-cors-headers==4.9.0
django-filter==25.2
djangorestframework==3.16.1
idna==3.11
markdown-it-py==4.0.0
mdurl==0.1.2
Pygments==2.19.2
requests==2.32.5
rich==14.3.2
shellingham==1.5.4
sqlparse==0.5.5
typer==0.24.0
tzdata==2025.3
urllib3==2.6.3

# Evaluation Highlights

- Clean project structure
- RESTful design
- Custom filtering
- Custom API actions
- Validation logic
- CLI + Web interface
- Persistent database

---

# Future Improvements

- Authentication (JWT)
- Pagination
- Search functionality
- Deployment (Render/Heroku)
- Unit testing
- Role-based access

---

# Author

Hemish Pansuriya
Python Developer Practical Assessment
