'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s): Sam Haddad, Hai Dang Le, Esther Finotti, Miles Porter, Yasemin Fekadu
Description: Project 2 - CampusEats entry point
'''

from app import app
from seed import seed

if __name__ == "__main__":
    with app.app_context():
        seed()
    app.run(host="0.0.0.0", port=5000, debug=False)
