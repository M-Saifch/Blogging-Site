from urllib.parse import urlsplit

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from app.extensions import db
from app.forms import LoginForm, RegistrationForm
from app.models import User

auth = Blueprint("auth", __name__)


def is_safe_next(target):
    """Allow only relative paths on our own site (blocks open redirects)."""
    if not target or not target.startswith("/"):
        return False
    if target.startswith("//") or "\\" in target:
        return False
    return urlsplit(target).netloc == ""


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data.lower(),
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created! You can now log in.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Welcome back, {user.username}!", "success")
            next_page = request.args.get("next")
            if is_safe_next(next_page):
                return redirect(next_page)
            return redirect(url_for("main.home"))
        flash("Invalid email or password.", "danger")
    return render_template("login.html", form=form)


@auth.route("/logout", methods=["POST"])
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.home"))