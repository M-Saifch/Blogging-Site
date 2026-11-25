from flask import Blueprint, current_app, render_template, request

from app.extensions import db
from app.models import Post

main = Blueprint("main", __name__)


@main.route("/")
def home():
    page = request.args.get("page", 1, type=int)
    pagination = db.paginate(
        db.select(Post).order_by(Post.created_at.desc(), Post.id.desc()),
        page=page,
        per_page=current_app.config["POSTS_PER_PAGE"],
    )
    return render_template("index.html", pagination=pagination)