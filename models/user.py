from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        # Implement your authentication logic here
        # For example, check if the user has valid credentials
        return True  # Return True if the user is authenticated

    def is_active(self):
        # Implement your logic to check if the user's account is active
        return True  # Return True if the user's account is active

    def is_anonymous(self):
        return False
