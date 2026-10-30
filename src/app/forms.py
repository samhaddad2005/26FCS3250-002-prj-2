from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SelectField,
    SubmitField,
    TextAreaField,
    IntegerField,
    DateTimeLocalField,
    SelectMultipleField
)
from wtforms.validators import DataRequired, Email, Length, ValidationError, NumberRange
from app import db
from app.models import User
from wtforms import widgets

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


class FoodListingForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    description = TextAreaField("Description", validators=[DataRequired()])
    portions = IntegerField("Portions", validators=[DataRequired(), NumberRange(min=1, max=100)])
    pickup_location = StringField("Pickup Location", validators=[DataRequired(), Length(max=200)])
    dietary_tags = SelectMultipleField(
        "Dietary Tags",
        choices=[
            ("vegetarian", "Vegetarian"),
            ("vegan", "Vegan"),
            ("gluten-free", "Gluten-Free"),
            ("halal", "Halal"),
            ("contains nuts", "Contains Nuts")
        ],
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput()
    )
    pickup_start = DateTimeLocalField("Pickup Start", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    pickup_end = DateTimeLocalField("Pickup End", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    submit = SubmitField("Create Listing")

    def validate_pickup_end(self, field):
        if field.data and self.pickup_start.data and field.data <= self.pickup_start.data:
            raise ValidationError("Pickup end must be after pickup start.")
        if field.data and field.data <= datetime.now():
          raise ValidationError("Pickup end must be in the future.")