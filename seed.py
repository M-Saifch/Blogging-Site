from werkzeug.security import generate_password_hash

from app import create_app
from app.extensions import db
from app.models import Post, User

app = create_app()

with app.app_context():
    if User.query.first():
        print("Database already has data, skipping.")
    else:
        user = User(
            username="saif",
            email="saif@example.com",
            password_hash=generate_password_hash("password123"),
        )
        db.session.add(user)
        db.session.commit()

        db.session.add(Post(title="My first post", body="Hello from the database!", user_id=user.id))
        db.session.add(Post(title="Learning Flask", body="Models make data persistent.", user_id=user.id))
        db.session.commit()
        print("Seeded 1 user and 2 posts.")