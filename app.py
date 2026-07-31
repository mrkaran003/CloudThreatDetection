from flask import Flask
from config import Config

from routes.auth import auth
from routes.dashboard import dashboard
from routes.upload import upload
from routes.history import history
from routes.report import report
from routes.profile import profile
from routes.settings import settings
from routes.admin import admin
from routes.files import files

from utils.database import (
    init_database,
    init_login,
    create_database,
    login_manager
)

from models.models import User, ThreatLog


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    @app.context_processor
    def global_notifications():

        recent_threats = ThreatLog.query.order_by(
            ThreatLog.detected_at.desc()
        ).limit(5).all()

        return {
            "recent_threats": recent_threats,
            "notification_count": len(recent_threats)
        }

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
    app.register_blueprint(settings)
    app.register_blueprint(admin)
    app.register_blueprint(files)

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