from .development import DevelopmentConfig
from .testing import TestingConfig

# Create a dictionary to hold all configurations
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
