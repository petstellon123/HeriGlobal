from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Include our Routes
        from .admin.routes import admin_bp
        from .api.routes import api_bp
        from .auth.routes import auth_bp

        # Register Blueprints
        app.register_blueprint(auth_bp)
        app.register_blueprint(api_bp, url_prefix='/api')
        app.register_blueprint(admin_bp, url_prefix='/admin')

        db.create_all()

        return app