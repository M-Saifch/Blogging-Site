from flask import Flask

from config import Config
from app.extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.main import main
    from app.routes.posts import posts
    app.register_blueprint(main)
    app.register_blueprint(posts)

    with app.app_context():
        from app import models  # noqa: F401
        db.create_all()

    return app