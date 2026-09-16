from datetime import datetime

from utils.database import db


class SecurityAlert(db.Model):
    __tablename__ = "security_alerts"

    id = db.Column(db.Integer, primary_key=True)

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    hostname = db.Column(
        db.String(255),
        nullable=False
    )

    operating_system = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    severity = db.Column(
        db.String(20),
        nullable=False
    )

    risk_score = db.Column(
        db.Integer,
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    evidence = db.Column(
        db.Text,
        nullable=True
    )

    status = db.Column(
        db.String(30),
        default="Open",
        nullable=False
    )

    def __repr__(self):
        return f"<SecurityAlert {self.id} {self.severity}>"