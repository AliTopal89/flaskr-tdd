#create_db.py

from app import db
from models import Flaskr

#create the database and the db table, creates all the tables on SQLAlchemy
db.create_all()

# session here is not the Flask session, but the Flask-SQLAlchemy one
db.session.commit()
