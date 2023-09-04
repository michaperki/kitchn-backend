from flask import Blueprint, jsonify, request
import pyrebase
import os
from dotenv import load_dotenv
from flask_cors import cross_origin

load_dotenv()
data_bp = Blueprint('data', __name__, url_prefix="/data")

firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()

# Create a new group and save it to Firebase Realtime Database
@data_bp.route('/create_group', methods=['POST'])
@cross_origin()
def create_group():
    try:
        # Parse the request JSON data
        data = request.json
        group_name = data.get('groupName')
        selected_friends = data.get('selectedFriends')

        # Create a new group object
        new_group = {
            'groupName': group_name,
            'selectedFriends': selected_friends
        }

        # Push the new group to the database
        new_group_ref = database.child('groups').push(new_group)

        # Return the ID of the newly created group
        return jsonify({'groupId': new_group_ref.key}, 201)

    except Exception as e:
        return jsonify({'error': str(e)}, 500)

@data_bp.route('/groups', methods=['GET'])
@cross_origin()
def get_groups():
    try:
        # Get a reference to the 'groups' node in Firebase
        groups_ref = database.child('groups')
        
        # Retrieve all groups from the 'groups' node
        groups = groups_ref.get().val()

        # Initialize an empty list to store group data
        group_data = []

        if groups:
            # Iterate through the retrieved groups and append them to the list
            for group_id, group in groups.items():
                group_data.append({"id": group_id, **group})

        return jsonify(group_data, 200)

    except Exception as e:
        return jsonify({'error': str(e)}, 500)