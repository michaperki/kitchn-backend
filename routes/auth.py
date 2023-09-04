from flask import Blueprint, request, jsonify
from extensions import db  # Import the db object and User model
from models.user import User  # Import the User model
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    # Get user registration data from the request
    data = request.json
    user = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if the email is already registered
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email already registered"}), 400

    # Create a new user
    new_user = User(email=email, user=user)
    new_user.set_password(password)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})

@auth_bp.route('/login', methods=['POST'])
def login():
    # Get login data from the request
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        # User exists and password is correct
        # You can implement token-based authentication here if needed
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Login failed"}), 401

@auth_bp.route('/protected', methods=['GET'])
def protected_route():
    # Implement protected route logic here
    return jsonify(message="This is a protected route")
