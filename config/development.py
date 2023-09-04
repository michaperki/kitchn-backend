# development.py

class DevelopmentConfig:
    # Flask App Configuration
    DEBUG = True  # Enable debug mode for development
    SECRET_KEY = 'your-secret-key'  # Replace with a strong, random secret key

    # Database Configuration (example for SQLAlchemy)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'  # SQLite database for development
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable SQLAlchemy event tracking for performance

    # Flask-Login Configuration (example)
    LOGIN_DISABLED = False  # Enable user authentication

    # CORS Configuration (if needed for frontend development)
    CORS_ALLOWED_ORIGINS = ['http://localhost:3000']  # Replace with your frontend URL
    
    JWT_SECRET_KEY = 'temp'
