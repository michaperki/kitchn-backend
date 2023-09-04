from flask import Flask
from flask_cors import CORS
from config import DevelopmentConfig, TestingConfig
from extensions import login_manager, db
from models.user import User
from routes import auth, data, errors
from dotenv import load_dotenv

def create_app(config_name='development'):
    app = Flask(__name__)
    CORS(app, resources={
        r"/auth/*": {"origins": ["https://michaperki.github.io", "http://localhost:3000"]},
        r"/api/*": {"origins": ["https://michaperki.github.io", "http://localhost:3000"]}
    })
        
    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'testing':
        app.config.from_object(TestingConfig)

    # Initialize database and authentication
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
        
    # Load env variables
    load_dotenv()

    # Register blueprints for routes
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(data.data_bp)
    app.register_blueprint(errors.errors_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app