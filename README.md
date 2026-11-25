# Blog Platform

A simple blog platform built with Flask where users can register, log in, and create, edit, delete and read blog posts. Built as a learning project to practice MVC architecture, authentication, authorization and database persistence.

## Features

- User registration and login (passwords hashed with Werkzeug, sessions handled by Flask-Login)
- Create, read, update and delete blog posts
- Authorization: only the author of a post can edit or delete it
- Form validation and CSRF protection with Flask-WTF
- Pagination, flash messages and custom 403 / 404 / 500 error pages
- SQLite database accessed through the SQLAlchemy ORM

## Tech Stack

Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, SQLite, Jinja2, HTML and CSS

## Screenshots

![Home page](screenshots/home.png)
![Post page](screenshots/post.png)
![Login page](screenshots/login.png)

## Getting Started

1. Clone the repository

   ```
   git clone https://github.com/M-Saifch/Blogging-Site.git
   cd Blogging-Site
   ```

2. Create and activate a virtual environment

   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. Install dependencies

   ```
   python -m pip install -r requirements.txt
   ```

4. Create your `.env` file from the example and set a secret key

   ```
   copy .env.example .env       # Windows
   cp .env.example .env         # macOS / Linux
   ```

   Generate a key with:

   ```
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

5. (Optional) Add demo data. This creates a demo user (`saif@example.com` / `password123`) and two posts

   ```
   python seed.py
   ```

6. Run the app

   ```
   python run.py
   ```

   Then open http://127.0.0.1:5000

> This project uses Flask's development server and is not configured for production deployment.

## Project Structure

```
Blog-Platform/
├── app/
│   ├── __init__.py        # application factory
│   ├── extensions.py      # db, csrf, login_manager
│   ├── models.py          # Model: User, Post
│   ├── forms.py           # WTForms: Post, Registration, Login
│   ├── routes/            # Controllers: main, posts, auth, errors
│   ├── templates/         # Views (Jinja2)
│   └── static/            # CSS
├── config.py
├── run.py
├── seed.py
├── requirements.txt
└── README.md
```

## MVC Mapping

| Layer | Where |
|---|---|
| Model | `app/models.py` |
| View | `app/templates/` |
| Controller | `app/routes/` |

## What I Learned

- Structuring a Flask app with an application factory and blueprints
- Modelling relationships (one user, many posts) with SQLAlchemy
- Password hashing, sessions and the difference between authentication and authorization
- Protecting forms with CSRF tokens and validating user input on the server
- Keeping secrets out of source control with environment variables

## Future Improvements

- Comments and post tags
- Search
- Markdown support for posts
- Database migrations with Flask-Migrate
- Automated tests
- Deployment