from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)  # Add this line
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        # Implement your authentication logic here
        # Check if the user has valid credentials or is authenticated in your system
        # For example, you might check if the user's session or token is valid
        return True  # Return True if the user is authenticated

    def is_active(self):
        # Implement your logic to check if the user's account is active
        # Check if the user's account is not banned or disabled, for instance
        return True  # Return True if the user's account is active

    def is_anonymous(self):
        # Implement your logic to check if the user is anonymous
        # This should return True if the user is not logged in or identified
        return False  # Return False if the user is not anonymous
