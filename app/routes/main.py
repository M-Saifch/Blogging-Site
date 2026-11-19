from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    # Temporary stand-in for the Model (real database comes in Step 3)
    posts = [
        {"title": "My first post", "body": "Hello from the blog platform!"},
        {"title": "Learning Flask", "body": "MVC makes code easier to organize."},
    ]
    return render_template("index.html", posts=posts)