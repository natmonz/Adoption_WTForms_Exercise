from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


DEFAULT_IMAGE = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3ANo_Image_Available.jpg&psig=AOvVaw3AuaTTsslZvsvRs3PfBxcc&ust=1687305280356000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNiQgJHE0P8CFQAAAAAdAAAAABAE'

class Pet(db.Model):
    ''''''
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement=True)
    
    name = db.Column(db.Text,
                     nullable=False)
    
    species = db.Column(db.Text,
                        nullable=False)
    
    photo_url = db.Column(db.Text)
    
    age = db.Column(db.Integer)
    
    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    
    def image_url(self):
        """return image of the pet"""
        return self.photo_url or DEFAULT_IMAGE


def connect_db(app):
    '''Connecting to the Database'''
    db.app = app
    db.init_app(app)