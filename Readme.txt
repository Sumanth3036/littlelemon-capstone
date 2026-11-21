Little Lemon back-end capstone
================================

Django REST Framework API for the Little Lemon restaurant. The API handles
menu items and table bookings, updates Django models, and stores data in a
MySQL database named reservations.

Setup
-----
1. Create a MySQL database named reservations.

   CREATE DATABASE reservations;

2. Create and activate a virtual environment, then install dependencies:

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. In littlelemon/settings.py, replace the PASSWORD placeholder ('password')
   with your MySQL root password if it is different.

4. Run migrations and create a superuser:

   python manage.py migrate
   python manage.py createsuperuser

5. Start the development server:

   python manage.py runserver

6. Open the static homepage at http://127.0.0.1:8000/restaurant/
   Django admin is available at http://127.0.0.1:8000/admin/

API paths to test with Insomnia
-------------------------------
GET  /restaurant/
     Static HTML homepage for Little Lemon.

GET, POST  /restaurant/menu/
     List all menu items, or create a new menu item.
     Example POST body (JSON):
     {
       "title": "Greek Salad",
       "price": "12.50",
       "inventory": 20
     }

GET, PUT, PATCH, DELETE  /restaurant/menu/<id>
     Retrieve, update, or delete a single menu item.
     Example: /restaurant/menu/1

GET, POST, PUT, PATCH, DELETE  /restaurant/booking/tables/
     Table booking API (ViewSet). Authentication required.
     Example POST body (JSON):
     {
       "name": "Aman",
       "no_of_guests": 4,
       "booking_date": "2026-12-01T19:00:00Z"
     }

POST  /auth/users/
     Register a new user with Djoser.
     Example body (JSON):
     {
       "username": "aman",
       "password": "StrongPass123",
       "email": "aman@example.com"
     }

POST  /auth/token/login/
     Obtain an authorization token with Djoser.
     Example body (JSON):
     {
       "username": "aman",
       "password": "StrongPass123"
     }

POST  /api-token-auth/
     Obtain an authorization token with Django REST Framework.
     Example body (JSON):
     {
       "username": "aman",
       "password": "StrongPass123"
     }

Authorization
-------------
Protected booking endpoints require a token header:

  Authorization: Token <token>

You can also generate a token for a user from the Django Admin interface
(Token section) after migrations have been applied.

Tests
-----
Unit tests live in the project-level package littlelemon/tests/.
The test runner uses SQLite automatically so MySQL is not required:

  python manage.py test

To force SQLite for other management commands (for example check, when
MySQL is not running):

  DJANGO_USE_SQLITE=1 python manage.py check
