from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": str(e)}).data
    response.status_code = e.code
    return response

@errors_bp.route('/error_example')
def error_example():
    # Simulate an error (for testing error handling)
    raise HTTPException("An example error occurred", 500)
