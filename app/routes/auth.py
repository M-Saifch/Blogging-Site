from flask import Blueprint, flash, redirect, render_template, url_for

from app.extensions import db
from app.forms import RegistrationForm
from app.models import User

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data.lower(),
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Login is coming in the next step.", "success")
        return redirect(url_for("main.home"))
    return render_template("register.html", form=form)