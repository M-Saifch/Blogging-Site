from flask import Blueprint, render_template

from app.extensions import db
from app.models import Post

posts = Blueprint("posts", __name__, url_prefix="/post")


@posts.route("/<int:post_id>")
def detail(post_id):
    post = db.get_or_404(Post, post_id)
    return render_template("post_detail.html", post=post)