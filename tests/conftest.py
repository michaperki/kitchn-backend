import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app('testing')  # Use the testing configuration
    with app.app_context():
        yield app
