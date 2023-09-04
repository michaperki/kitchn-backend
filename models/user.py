from extensions import db  # Import the SQLAlchemy db object
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """
    Define the User model for the database.
    """

    __tablename__ = 'users'  # Name of the database table

    id = db.Column(db.Integer, primary_key=True)  # Primary key field
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email field
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username field
    password_hash = db.Column(db.String(128), nullable=False)  # Password hash field

    def __init__(self, email, username, password):
        """
        Initialize a new User object.

        :param email: The user's email address.
        :param username: The user's username.
        :param password: The user's password (plain text).
        """
        self.email = email
        self.username = username
        self.set_password(password)  # Hash and store the password

    def set_password(self, password):
        """
        Hash and set the user's password.

        :param password: The user's password (plain text).
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if a provided password matches the user's stored password hash.

        :param password: The password to check (plain text).
        :return: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        Return a string representation of the User object.

        :return: A string representation.
        """
        return f"<User {self.id}: {self.username}>"
