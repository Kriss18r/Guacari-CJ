from flask import Flask
from .extensions import db
from .routes import main_bp
from .auth import auth_bp
from .admin import admin_bp

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object('config.Config')

    # extensiones
    db.init_app(app)

    # blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    # crear tablas
    with app.app_context():
        db.create_all()

    return app
