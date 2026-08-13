# Jewelify Auth

A simple Django authentication demo built as an internship project.

## Overview

This project implements a basic user registration and login system using Django with SQLite. It includes templates for:

- Register
- Login
- Logout
- Account page
- Forgot password
- Email verification page
- Reset password
- Two-step verification page

## Project Structure

- `application/` - Django app containing views, models, templates, and URLs
- `project/` - Django project configuration
- `db.sqlite3` - SQLite database file
- `manage.py` - Django management utility

## Features

- User registration
- User login
- Session-based authentication
- Account page access control
- Password reset workflow
- Static templates for auth pages

## Requirements

- Python 3.10+ (recommended)
- Django 6.0.x

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - Windows:
     ```powershell
     .\venv\Scripts\Activate
     ```

3. Install Django:

   ```bash
   pip install django==6.0.3
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser:

   ```text
   http://127.0.0.1:8000/
   ```

## GitHub / Git

1. Create a `.gitignore` file with at least the following entries:

   ```gitignore
   venv/
   __pycache__/
   *.pyc
   db.sqlite3
   *.sqlite3
   .env
   *.log
   ```

2. Generate `requirements.txt` from your active environment:

   ```bash
   pip freeze > requirements.txt
   ```

3. Initialize Git and make the first commit:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```

## Deployment

For a simple live deployment, use a platform like Render or PythonAnywhere.

- Set `DEBUG = False` in `project/settings.py`.
- Add your host to `ALLOWED_HOSTS`.
- Never store `SECRET_KEY` in source control; use environment variables instead.
- Install from `requirements.txt` with:

  ```bash
  pip install -r requirements.txt
  ```

- If using Render, use a start command such as:

  ```bash
  gunicorn project.wsgi:application --bind 0.0.0.0:$PORT
  ```

## Notes

- The app uses SQLite by default (`db.sqlite3`).
- Passwords are stored in plain text in the database, which is insecure. Do not use this implementation in production.
- `DEBUG` is set to `True` in `project/settings.py`, which is also for development only.

## Optional

To create a superuser for admin access:

```bash
python manage.py createsuperuser
```

Then visit:

```text
http://127.0.0.1:8000/admin/
```

## App URLs

- `/` - Home page
- `/register/` - Registration page
- `/login/` - Login page
- `/logout/` - Logout endpoint
- `/account/` - Account page
- `/forgot-password/` - Forgot password page
- `/email-sent/` - Email verification placeholder page
- `/two-factor-authentication/` - Two-step verification page
- `/reset-password/` - Password reset page


NOTE : Forgot password / Reset password did't Functioning so, ignore it.
