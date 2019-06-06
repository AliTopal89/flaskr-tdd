from app import db

# Since a person with no name or an email address with no address associated makes no sense, 
# nullable=False tells SQLAlchemy to create the column as NOT NULL
class Flaskr(db.Model):

    __tablename__ = "flaskr"

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text
    
    def __repr__(self):
        return '<title {}>'.format(self.body)
