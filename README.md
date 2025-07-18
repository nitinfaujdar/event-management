# 🗓️ Event Management System API

A mini event management backend built with Django REST Framework using clean architecture.

---

## 🚀 Features

- Create events with max capacity and time slots
- Register attendees per event (no duplicates or overbooking)
- View upcoming events and attendee lists
- Timezone support (IST)
- Swagger UI for API exploration
- Pagination for attendees
- Modular code structure
- Unit tested with pytest

---

## 📦 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL or SQLite
- drf-yasg for Swagger UI
- pytest for testing

---

## 🔧 Setup Instructions

git clone https://github.com/nitinfaujdar/event-management/

cd event_management

python -m venv venv

source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

🌐 API Docs

Swagger UI: http://localhost:8000/swagger/

ReDoc UI: http://localhost:8000/redoc/

| Method | Endpoint                 | Description                     |
| ------ | ------------------------ | ------------------------------- |
| POST   | `/events`                | Create a new event              |
| GET    | `/events/`               | List upcoming events            |
| POST   | `/events/{id}/register`  | Register an attendee            |
| GET    | `/events/{id}/attendees` | List all attendees for an event |
