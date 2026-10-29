from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from app import db
from app.models import User


class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    password_confirm= PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8)])
    role = SelectField("I am a", choices=[("student", "Student"), ("vendor", "Vendor")])
    submit = SubmitField("Register")

    def validate_email(self, field):
        email = field.data.strip().lower()
        if db.session.scalar(db.select(User).filter_by(email=email)):
            raise ValidationError("That email is already registered.")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")