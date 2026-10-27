from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

# many-to-many link between listings and dietary tags
listing_tags = db.Table(
    "listing_tags",
    db.Column("listing_id", db.Integer, db.ForeignKey("listing.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("dietary_tag.id"), primary_key=True),
)


class User(UserMixin, db.Model):
    __tablename__ = "users"  # "user" is a reserved word in Postgres

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "student" or "vendor"

    listings = db.relationship("Listing", back_populates="vendor")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class DietaryTag(db.Model):
    __tablename__ = "dietary_tag"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    listings = db.relationship("Listing", secondary=listing_tags, back_populates="tags")


class Listing(db.Model):
    __tablename__ = "listing"

    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    portions_total = db.Column(db.Integer, nullable=False)
    portions_remaining = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    window_start = db.Column(db.DateTime, nullable=False)
    window_end = db.Column(db.DateTime, nullable=False)
    cancelled = db.Column(db.Boolean, nullable=False, default=False)

    vendor = db.relationship("User", back_populates="listings")
    tags = db.relationship("DietaryTag", secondary=listing_tags, back_populates="listings")


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))