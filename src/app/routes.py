from flask import render_template, redirect, url_for, flash, abort,request
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db
from app.forms import SignUpForm, LoginForm, FoodListingForm, ConfirmPickupForm, CancelReservationForm
from app.models import User, FoodListing, Reservation

import secrets
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from datetime import datetime, timedelta

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
    selected_tags = request.args.getlist("tags")
    selected_location = request.args.get("location")
    available = db.session.scalars(FoodListing.available()).all()
    if selected_tags:
        available = [
            listing for listing in available
            if all(
                tag in (listing.dietary_tags or "").split(",")
                or (
                    tag == "vegetarian"
                    and "vegan" in (listing.dietary_tags or "").split(",")
                )
                for tag in selected_tags
            )
        ]
    if selected_location:
        available = [
            listing for listing in available
            if selected_location.lower() in listing.pickup_location.lower()
        ]
    return render_template(
        "listings.html",
         listings=available,
         selected_tags=selected_tags,
         selected_location=selected_location
)


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
    return render_template(
        "reservation_success.html",
        pickup_code=pickup_code
        ), 201

@app.route("/confirm_pickup", methods=["GET", "POST"])
@login_required
def confirm_pickup():
    if current_user.role != "vendor":
        abort(403)

    update_no_shows()

    form = ConfirmPickupForm()
    if form.validate_on_submit():
        reservation = db.session.scalar(
            db.select(Reservation)
            .join(FoodListing, Reservation.listing_id == FoodListing.id)
            .where(
                Reservation.pickup_code == form.pickup_code.data,
                FoodListing.vendor_id == current_user.id,
            )
            .with_for_update()
        )

        if reservation is None:
            flash("No reservation with that pickup code was found for your listings.")
        elif reservation.status != "active":
            flash("This reservation is no longer active.")
        else:
            listing = db.session.get(FoodListing, reservation.listing_id)
            now = datetime.now()

            if listing.cancelled:
                flash("This listing was cancelled.")
            elif now < listing.pickup_start:
                flash("This pickup window has not started yet.")
            elif listing.pickup_end <= now:
                flash("The pickup window has ended.")
            else:
                student = db.session.get(User, reservation.student_id)
                message = (
                    f"Pickup confirmed for {student.name}. "
                    f"Portions to hand out: {reservation.portions}"
                )
                reservation.status = "picked_up"
                db.session.commit()
                flash(message)
                return redirect(url_for("confirm_pickup"))

    no_shows = db.session.execute(
        db.select(
            FoodListing.title.label("listing_title"),
            User.name.label("student_name"),
            Reservation.portions,
        )
        .select_from(Reservation)
        .join(FoodListing, Reservation.listing_id == FoodListing.id)
        .join(User, Reservation.student_id == User.id)
        .where(
            FoodListing.vendor_id == current_user.id,
            Reservation.status == "no-show",
            FoodListing.cancelled.is_(False)
        )
        .order_by(FoodListing.pickup_end.desc(), Reservation.id)
    ).all()

    return render_template(
        "confirm_pickup.html", form=form, no_shows=no_shows
    )

# US6: Display reservations belonging to the logged-in student.
@app.route("/my_reservations")
@login_required
def my_reservations():
    if current_user.role != "student":
        abort(403)
    
    update_no_shows()

    reservations = db.session.scalars(
        db.select(Reservation).where(
            Reservation.student_id == current_user.id
        )
    ).all()

    # Create a CSRF-protected cancellation form.
    cancel_form = CancelReservationForm()

    # Pass reservations, cancellation form, and current time to Jinja.
    return render_template(
        "my_reservations.html",
        reservations=reservations,
        cancel_form=cancel_form,
        now=datetime.now()
    )

# US6: Cancel a student's reservation.
@app.route("/cancel_reservation/<int:reservation_id>", methods=["POST"])
@login_required
def cancel_reservation(reservation_id):
    if current_user.role != "student":
        abort(403)

    form = CancelReservationForm()
    if not form.validate_on_submit():
        abort(400, description="Invalid or missing CSRF token.")
    
    # Find the reservation before accessing its listing_id.
    reservation = db.session.get(Reservation, reservation_id)
    if reservation is None:
        abort(404)
    if reservation.student_id != current_user.id:
        abort(403)

    # Lock the food listing before modifying its portions.
    listing = db.session.scalar(
        db.select(FoodListing)
        .where(FoodListing.id == reservation.listing_id)
        .with_for_update()
    )

    # Lock and reload the reservation.
    db.session.expire(reservation)
    reservation = db.session.scalar(
        db.select(Reservation)
        .where(Reservation.id == reservation_id)
        .with_for_update()
    )

    # Validate reservation cancellation eligibility
    if reservation.status != "active":
        db.session.rollback()
        abort(409, description="Reservation is not active.")
    if reservation.listing.pickup_end <= datetime.now():
        db.session.rollback()
        abort(409, description="Pickup window has ended.")

    # Cancel the reservation and restore available portions
    listing.portions_remaining += reservation.portions
    reservation.status = "cancelled"
    db.session.commit()

    # Return to My Reservations.
    flash("Reservation cancelled successfully.")
    return redirect(url_for("my_reservations"))

def update_no_shows():
    now = datetime.now()

    reservations = db.session.scalars(
        db.select(Reservation)
        .join(FoodListing, Reservation.listing_id == FoodListing.id)
        .where(
            Reservation.status == "active",
            FoodListing.pickup_end <= now,
            FoodListing.cancelled.is_(False)
        )
        .with_for_update(of=Reservation)
    ).all()

    for reservation in reservations:
        reservation.status = "no-show"
    db.session.commit()

# US9: Vendor impact dashboard
@app.route("/impact_dashboard")
@login_required
def impact_dashboard():
    if current_user.role != "vendor":
        abort(403)
    update_no_shows()
    start_date = request.args.get("start_date", "")
    end_date = request.args.get("end_date", "")
    filters = [FoodListing.vendor_id == current_user.id]
    try:
        if start_date:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            filters.append(FoodListing.created_at >= start)

        if end_date:
            end = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)
            filters.append(FoodListing.created_at < end)

    except ValueError:
        abort(400, description="Invalid date format.")
    listings_posted = db.session.scalar(
        db.select(func.count(FoodListing.id))
        .where(*filters)
    ) or 0

    portions_posted = db.session.scalar(
        db.select(func.sum(FoodListing.portions))
        .where(*filters)
    ) or 0
    rescued_portions = db.session.scalar(
        db.select(func.sum(Reservation.portions))
        .join(FoodListing, Reservation.listing_id == FoodListing.id)
        .where(
            *filters,
            Reservation.status == "picked_up"
        )
    ) or 0
    no_show_count = db.session.scalar(
        db.select(func.count(Reservation.id))
        .join(FoodListing, Reservation.listing_id == FoodListing.id)
        .where(
            *filters,
            Reservation.status == "no-show"
        )
    ) or 0
    no_show_portions = db.session.scalar(
        db.select(func.sum(Reservation.portions))
        .join(FoodListing, Reservation.listing_id == FoodListing.id)
        .where(
            *filters,
            Reservation.status == "no-show"
        )
    ) or 0

    reserved_portions = db.session.scalar(
        db.select(func.sum(Reservation.portions))
        .join(FoodListing, Reservation.listing_id == FoodListing.id)
        .where(
            *filters,
            Reservation.status != "cancelled"
        )
    ) or 0
    no_show_rate = (no_show_portions / reserved_portions * 100) if reserved_portions else 0
    return render_template(
        "impact_dashboard.html",
        start_date=start_date,
        end_date=end_date,
        listings_posted=listings_posted,
        portions_posted=portions_posted,
        rescued_portions=rescued_portions,
        no_show_count=no_show_count,
        no_show_rate=no_show_rate
    )