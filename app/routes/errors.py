from flask import Blueprint, render_template

from app.extensions import db

errors = Blueprint("errors", __name__)


def render_error(code, title, message):
    return render_template("error.html", code=code, title=title, message=message), code


@errors.app_errorhandler(403)
def forbidden(error):
    return render_error(403, "Forbidden", "You don't have permission to do that.")


@errors.app_errorhandler(404)
def not_found(error):
    return render_error(404, "Page not found", "The page you are looking for doesn't exist.")


@errors.app_errorhandler(500)
def server_error(error):
    db.session.rollback()
    return render_error(500, "Server error", "Something went wrong on our side.")