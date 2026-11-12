from datetime import datetime
from flask_login import UserMixin
import bcrypt
from app import db, login_manager



class User(UserMixin, db.Model):
    __tablename__ = "users"  # "user" is a reserved word in Postgres

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "student" or "vendor"


    def set_password(self, password):
        self.password_hash =  bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
    def check_password(self,  password):
        return bcrypt.checkpw(password.encode("utf-8"),self.password_hash.encode("utf-8"))


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))



class FoodListing(db.Model):
    __tablename__ = "food_listings"
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description= db.Column(db.Text, nullable=False)
    portions = db.Column(db.Integer, nullable=False)
    portions_remaining = db.Column(db.Integer, nullable=False)
    cancelled = db.Column(db.Boolean, nullable=False, default=False)
    pickup_location = db.Column(db.String(200), nullable=False)
    dietary_tags = db.Column(db.String(200))
    pickup_start = db.Column(db.DateTime, nullable=False)
    pickup_end = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.now)
    vendor = db.relationship("User")

    @classmethod
    def available(cls):
        return (
            db.select(cls)
            .where(
                cls.pickup_end > datetime.now(),
                cls.portions_remaining > 0,
                cls.cancelled.is_(False),
            )
            .order_by(cls.pickup_end, cls.id)
        )

class Reservation(db.Model):
    __tablename__ = "reservation"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    listing_id = db.Column(
        db.Integer,
        db.ForeignKey("food_listings.id"),
        nullable=False
    )
    pickup_code = db.Column(
        db.String(6),
        unique=True,
        nullable=False
    )
    portions = db.Column(db.Integer, nullable=False)
    status = db.Column(
        db.String(20),
        nullable=False,
        default="active"
    )
    # US6: Connect each reservation to its food listing.
    listing = db.relationship("FoodListing")


