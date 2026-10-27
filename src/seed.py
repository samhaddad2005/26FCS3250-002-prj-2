'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s): Sam Haddad, Hai Dang Le, Esther Finotti, Miles Porter, Yasemin Fekadu
Description: Project 2 - CampusEats demo seed data
'''

from datetime import datetime, timedelta

from app import db
from app.models import User, DietaryTag, Listing

TAG_NAMES = ["vegetarian", "vegan", "gluten-free", "halal", "contains nuts"]

# DEMO ONLY: these accounts exist so the app can be graded without manual data entry
SEED_USERS = [
    {"name": "Demo Vendor", "email": "vendor@campuseats.test", "password": "demo-vendor-pass", "role": "vendor"},
    {"name": "Demo Student", "email": "student@campuseats.test", "password": "demo-student-pass", "role": "student"},
]

# start and end are hours from now, so pickup windows are always in the future when created
SEED_LISTINGS = [
    {"title": "Veggie Wraps", "description": "Leftover wraps from the lunch rush.", "portions": 10,
     "location": "Tivoli Student Union", "start": 1, "end": 3, "tags": ["vegetarian"]},
    {"title": "Chicken Rice Bowls", "description": "Halal chicken over rice.", "portions": 6,
     "location": "Science Building Cafe", "start": 2, "end": 5, "tags": ["halal", "gluten-free"]},
    {"title": "Trail Mix Cups", "description": "Individually packed trail mix.", "portions": 20,
     "location": "Library Coffee Bar", "start": 24, "end": 48, "tags": ["vegan", "contains nuts"]},
]


def seed():
    '''Insert demo tags, accounts and listings, skipping any that already exist.
    Must be called inside app.app_context().'''
    tags = {}
    for name in TAG_NAMES:
        tag = db.session.scalar(db.select(DietaryTag).filter_by(name=name))
        if tag is None:
            tag = DietaryTag(name=name)
            db.session.add(tag)
        tags[name] = tag

    users = {}
    for data in SEED_USERS:
        user = db.session.scalar(db.select(User).filter_by(email=data["email"]))
        if user is None:
            user = User(name=data["name"], email=data["email"], role=data["role"])
            user.set_password(data["password"])
            db.session.add(user)
        users[data["role"]] = user

    db.session.flush()  # assigns ids to new users so the listing lookup works

    vendor = users["vendor"]
    now = datetime.now()
    for data in SEED_LISTINGS:
        listing = db.session.scalar(
            db.select(Listing).filter_by(vendor_id=vendor.id, title=data["title"])
        )
        if listing is None:
            db.session.add(Listing(
                vendor=vendor,
                title=data["title"],
                description=data["description"],
                portions_total=data["portions"],
                portions_remaining=data["portions"],
                location=data["location"],
                window_start=now + timedelta(hours=data["start"]),
                window_end=now + timedelta(hours=data["end"]),
                tags=[tags[name] for name in data["tags"]],
            ))

    db.session.commit()

    print("Seed accounts (DEMO ONLY):", flush=True)
    for data in SEED_USERS:
        print(f"  {data['role']}: {data['email']} / {data['password']}", flush=True)
