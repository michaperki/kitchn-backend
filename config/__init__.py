from .development import DevelopmentConfig
from .testing import TestingConfig
from .production import ProductionConfig

# Create a dictionary to hold all configurations
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
