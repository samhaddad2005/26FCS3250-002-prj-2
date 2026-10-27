'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s): Sam Haddad, Hai Dang Le, Esther Finotti, Miles Porter, Yasemin Fekadu
Description: Project 2 - CampusEats
'''

from flask import Flask
import os


app = Flask(__name__, template_folder="../../templates", static_folder="../../static")
app.secret_key = os.getenv("SECRET_KEY")

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)



from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from app import models
with app.app_context():
    db.create_all()
    
from app import routes

