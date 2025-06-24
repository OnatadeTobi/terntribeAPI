# TernTribe API
A simple RESTful API to manage social causes and contributions.

## Tech Stack
- Python
- Django
- Django REST Framework

## Features
- CRUD operations on causes
- Accept contributions for specific causes

## API Endpoints
- `POST /api/causes/`
- `GET /api/causes/`
- `GET /api/causes/<id>/`
- `PUT /api/causes/<id>/`
- `DELETE /api/causes/<id>/`
- `POST /api/causes/<id>/contribute/`

## How to Run
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Approach
- Used Django REST Framework for clean and scalable API development.
- Designed relational models to associate contributions to causes.
- Used class-based generic views for clarity and maintainability.


