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