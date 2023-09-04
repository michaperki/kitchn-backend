# models/user.py
from extensions import db

class Pet(db.Model):
    # User model definition here
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(64), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    breed = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    