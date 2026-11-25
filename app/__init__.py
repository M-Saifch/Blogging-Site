from flask import Flask

from config import Config
from app.extensions import csrf, db, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    from app.routes.main import main
    from app.routes.posts import posts
    from app.routes.auth import auth
    from app.routes.errors import errors
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(auth)
    app.register_blueprint(errors)

    with app.app_context():
        from app import models  # noqa: F401
        db.create_all()

    return app