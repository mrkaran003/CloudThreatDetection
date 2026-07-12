from datetime import datetime
from flask_login import UserMixin
from utils.database import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    username = db.Column(db.String(50), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), default="User")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class UploadedFile(db.Model):

    __tablename__ = "uploaded_files"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255), nullable=False)

    uploaded_by = db.Column(db.String(100))

    file_size = db.Column(db.Integer, default=0)

    file_type = db.Column(db.String(50))

    status = db.Column(db.String(50), default="Pending")

    upload_time = db.Column(db.DateTime, default=datetime.utcnow)


class ThreatLog(db.Model):

    __tablename__ = "threat_logs"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255), nullable=False)

    threat_type = db.Column(db.String(100))

    severity = db.Column(db.String(30))

    prediction = db.Column(db.String(50))

    confidence = db.Column(db.Float)

    remarks = db.Column(db.String(255))

    detected_at = db.Column(db.DateTime, default=datetime.utcnow)