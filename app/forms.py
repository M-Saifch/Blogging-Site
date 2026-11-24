from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    ValidationError,
)

from app.models import User


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=150)])
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Save")


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        filters=[lambda value: value.strip() if value else value],
        validators=[DataRequired(), Length(min=3, max=50)],
    )
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password", message="Passwords must match.")],
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("That username is already taken.")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("An account with that email already exists.")