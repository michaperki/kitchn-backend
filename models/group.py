from extensions import db  # Import the SQLAlchemy db object

class Group(db.Model):
    """
    Define the Group model for the database.
    """

    __tablename__ = 'groups'  # Name of the database table

    id = db.Column(db.Integer, primary_key=True)  # Primary key field
    group_name = db.Column(db.String(255), nullable=False)  # Group name field
    selected_friends = db.Column(db.JSON, nullable=False)  # JSON field to store selected friends

    def __init__(self, group_name, selected_friends):
        """
        Initialize a new Group object.

        :param group_name: The name of the group.
        :param selected_friends: A list of selected friend data.
        """
        self.group_name = group_name
        self.selected_friends = selected_friends

    def __repr__(self):
        """
        Return a string representation of the Group object.

        :return: A string representation.
        """
        return f"<Group {self.id}: {self.group_name}>"
