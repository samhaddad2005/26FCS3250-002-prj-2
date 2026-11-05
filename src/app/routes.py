from flask import render_template, redirect, url_for, flash, abort, request
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db
from app.forms import SignUpForm, LoginForm, FoodListingForm
from app.models import User, FoodListing, Reservation

import secrets
from sqlalchemy.exc import IntegrityError

from datetime import datetime

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
            portions_remaining=form.portions.data,
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


@app.route("/listings")
@login_required
def listings():
    if current_user.role != "student":
        abort(403)
    available = db.session.scalars(FoodListing.available()).all()
    return render_template("listings.html", listings=available)


# US4: Generate a unique six-digit pickup code for a reservation.
def generate_pickup_code():
    for _ in range(10):
        code = f"{secrets.randbelow(1000000):06d}"

        existing = db.session.scalar(
            db.select(Reservation.id).where(
                Reservation.pickup_code == code
            )
        )

        if existing is None:
            return code

    raise RuntimeError("Unable to generate a unique pickup code.")

# US4: Reserve food portions.
@app.route("/reserve/<int:listing_id>", methods=["POST"])
@login_required
def reserve(listing_id):
    if current_user.role != "student":
        abort(403)
    
    # Lock the listing to prevent concurrent overbooking.
    listing = db.session.scalar(
        db.select(FoodListing)
        .where(FoodListing.id == listing_id)
        .with_for_update() # Lock
    )
    if listing is None:
        db.session.rollback()
        abort(404)

    # Reject cancelled or expired listings.
    if listing.cancelled or listing.pickup_end <= datetime.now():
        db.session.rollback()
        abort(409, description="This listing is no longer available.")

    # Validate the requested number of portions.
    try:
        portions = int(request.form.get("portions", ""))
    except (ValueError, TypeError):
        db.session.rollback()
        abort(400, description="Invalid number of portions.")

    if portions not in (1, 2):
        db.session.rollback()
        abort(400, description="You can reserve only 1 or 2 portions.")

    # Reject requests that exceed the remaining portions.
    if portions > listing.portions_remaining:
        db.session.rollback()
        abort(409, description="Not enough portions remaining.")
    
    # Check whether the student already has an active reservation.
    existing_reservation = db.session.scalar(
        db.select(Reservation).where(
            Reservation.student_id == current_user.id,
            Reservation.listing_id == listing_id,
            Reservation.status == "active"
        )
    )
    if existing_reservation is not None:
        db.session.rollback()
        abort(409, description="You already have an active reservation.")

    # Generate a six-digit pickup code.
    try:
        pickup_code = generate_pickup_code()
    except RuntimeError:
        db.session.rollback() # Release the database lock.
        abort(503, description="Unable to generate a pickup code. Please try again.")


    # Decrease the remaining portions.
    listing.portions_remaining -= portions

    # Create the reservation.
    reservation = Reservation(
        student_id=current_user.id,
        listing_id=listing_id,
        portions=portions,
        pickup_code=pickup_code,
        status="active"
    )

    # Save the reservation and listing update together.
    db.session.add(reservation)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(409, description="Reservation could not be completed.")
    return f"Reservation successful! Pickup code: {pickup_code}", 201