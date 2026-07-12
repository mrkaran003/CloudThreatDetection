from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message = "Please login to continue."


def init_database(app):
    db.init_app(app)


def init_login(app):
    login_manager.init_app(app)


def create_database(app):
    with app.app_context():
        db.create_all()