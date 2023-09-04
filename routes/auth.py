from flask import Blueprint, request, jsonify
from extensions import db  # Import the db object and User model
from models.user import User  # Import the User model
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    # Get user data from the request
    data = request.json
    email = data.get('email')
    username = data.get('username')  # Ensure you get the username from the request
    password = data.get('password')

    # Check if the required fields are provided
    if not email or not username or not password:
        return jsonify({'message': 'Please provide all required fields.'}), 400

    # Create a new user record
    user = User(email=email, username=username)
    user.set_password(password)

    # Add the user to the database and commit the transaction
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of an error
        return jsonify({'message': 'An error occurred while registering the user.'}), 500

if __name__ == '__main__':
    app.run()

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
