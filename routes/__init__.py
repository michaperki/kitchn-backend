from flask import Blueprint

# Create Blueprint instances for different parts of your application
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
data_bp = Blueprint('data', __name__, url_prefix='/data')
errors_bp = Blueprint('errors', __name__)

# Import route handlers from individual modules
from . import auth, data, errors