from flask import Blueprint, jsonify, request
from models import Group  # Import your Group model
from extensions import db
from flask_cors import cross_origin

data_bp = Blueprint('data', __name__, url_prefix="/data")

# Create a new group and save it to the PostgreSQL database
@data_bp.route('/create_group', methods=['POST'])
@cross_origin()
def create_group():
    try:
        # Parse the request JSON data
        data = request.json
        group_name = data.get('groupName')
        selected_friends = data.get('selectedFriends')

        # Create a new group object
        new_group = Group(group_name=group_name, selected_friends=selected_friends)

        # Add the new group to the database
        db.session.add(new_group)
        db.session.commit()

        # Return the ID of the newly created group
        return jsonify({'groupId': new_group.id}, 201)

    except Exception as e:
        return jsonify({'error': str(e)}, 500)

@data_bp.route('/groups', methods=['GET'])
@cross_origin()
def get_groups():
    try:
        # Query all groups from the database
        groups = Group.query.all()

        # Initialize an empty list to store group data
        group_data = []

        # Iterate through the retrieved groups and append them to the list
        for group in groups:
            group_data.append({
                "id": group.id,
                "groupName": group.group_name,
                "selectedFriends": group.selected_friends
            })

        return jsonify(group_data, 200)

    except Exception as e:
        return jsonify({'error': str(e)}, 500)
