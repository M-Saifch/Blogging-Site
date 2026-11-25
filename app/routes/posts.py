from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from app.extensions import db
from app.forms import PostForm
from app.models import Post 

posts = Blueprint("posts", __name__, url_prefix="/post")


@posts.route("/<int:post_id>")
def detail(post_id):
    post = db.get_or_404(Post, post_id)
    return render_template("post_detail.html", post=post)


@posts.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Post created!", "success")
        return redirect(url_for("posts.detail", post_id=post.id))
    return render_template("post_form.html", form=form, heading="New Post")


@posts.route("/<int:post_id>/edit", methods=["GET", "POST"])
def edit(post_id):
    post = db.get_or_404(Post, post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        flash("Post updated!", "success")
        return redirect(url_for("posts.detail", post_id=post.id))
    return render_template("post_form.html", form=form, heading="Edit Post")


@posts.route("/<int:post_id>/delete", methods=["POST"])
def delete(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted.", "success")
    return redirect(url_for("main.home"))

