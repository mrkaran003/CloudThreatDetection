import os
from datetime import timedelta

# Base Directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Global Configuration"""

    # Flask
    SECRET_KEY = "CloudThreatDetection2026SecretKey"

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Uploads
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024

    ALLOWED_EXTENSIONS = {"csv", "txt", "log"}

    # Machine Learning
    MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

    # Reports
    REPORT_FOLDER = os.path.join(BASE_DIR, "reports")
    PDF_FOLDER = os.path.join(REPORT_FOLDER, "pdf")
    EXCEL_FOLDER = os.path.join(REPORT_FOLDER, "excel")
    CHART_FOLDER = os.path.join(REPORT_FOLDER, "charts")

    # Logs
    LOG_FOLDER = os.path.join(BASE_DIR, "logs")
    APP_LOG = os.path.join(LOG_FOLDER, "application.log")
    SECURITY_LOG = os.path.join(LOG_FOLDER, "security.log")
    THREAT_LOG = os.path.join(LOG_FOLDER, "threats.log")

    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

    # Application
    APP_NAME = "Cloud-Based Cyber Threat Detection"
    VERSION = "1.0.0"
    DEBUG = True