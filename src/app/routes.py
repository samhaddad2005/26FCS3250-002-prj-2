from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db
from app.forms import SignUpForm, LoginForm, FoodListingForm
from app.models import User, FoodListing

@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        if form.password.data != form.password_confirm.data:
            form.password_confirm.errors.append('Passwords do not match.')
        elif db.session.scalar(db.select(User).filter_by(email=email)):
            form.email.errors.append('That email is already taken.')
        else:
            user = User(email=email, name=form.name.data,role= form.role.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        user = db.session.scalar(db.select(User).filter_by(email=email))
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password.")
        else:
            login_user(user)
            return redirect(url_for("index"))
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
@app.route("/create_listing", methods=["GET", "POST"])
@login_required
def create_listing():
    if current_user.role != "vendor":
        abort(403)
    form = FoodListingForm()
    if form.validate_on_submit():
        listing = FoodListing(
            vendor_id=current_user.id,
            title=form.title.data,
            description=form.description.data,
            portions=form.portions.data,
            pickup_location=form.pickup_location.data,
            dietary_tags= ",".join(form.dietary_tags.data),
            pickup_start=form.pickup_start.data,
            pickup_end=form.pickup_end.data
        )
        db.session.add(listing)
        db.session.commit()
        flash("Food listing created successfully.")
        return redirect(url_for("index"))
    return render_template("create_listing.html", form=form)
