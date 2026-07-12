from flask import Flask
from config import Config
from routes.dashboard import dashboard
from routes.upload import upload
from routes.history import history
from routes.report import report
from routes.profile import profile

from utils.database import (
    init_database,
    init_login,
    create_database,
    login_manager
)

from models.models import User

from routes.auth import auth


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Extensions
    init_database(app)
    init_login(app)

    # Register Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(upload)
    app.register_blueprint(history)
    app.register_blueprint(report)
    app.register_blueprint(profile)
    # Create Database
    create_database(app)

    return app


app = create_app()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
print(app.url_map)


if __name__ == "__main__":
    app.run(debug=True)
    