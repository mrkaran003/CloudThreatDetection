from flask import Blueprint, render_template
from flask_login import login_required
from datetime import datetime

from models.models import UploadedFile, ThreatLog

dashboard = Blueprint(
    "dashboard",
    __name__
)


@dashboard.route("/")
@login_required
def home():

    total_files = UploadedFile.query.count()

    total_threats = ThreatLog.query.count()

    critical_risk = ThreatLog.query.filter_by(
        severity="Critical"
    ).count()

    high_risk = ThreatLog.query.filter_by(
        severity="High"
    ).count()

    medium_risk = ThreatLog.query.filter_by(
        severity="Medium"
    ).count()

    low_risk = ThreatLog.query.filter_by(
        severity="Low"
    ).count()

    safe_logs = max(
        total_files - total_threats,
        0
    )

    risk_score = 0

    if total_files > 0:
        risk_score = round(
            (total_threats / total_files) * 100,
            1
        )

    ai_engine = "Online"
    database = "Connected"
    cloud_server = "Running"
    scanner = "Active"

    last_scan = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    recent_threats = ThreatLog.query.order_by(
        ThreatLog.detected_at.desc()
    ).limit(8).all()

    notification_count = len(recent_threats)

    return render_template(
        "dashboard.html",

        total_files=total_files,
        total_threats=total_threats,

        critical_risk=critical_risk,
        high_risk=high_risk,
        medium_risk=medium_risk,
        low_risk=low_risk,

        safe_logs=safe_logs,
        risk_score=risk_score,

        ai_engine=ai_engine,
        database=database,
        cloud_server=cloud_server,
        scanner=scanner,

        last_scan=last_scan,

        recent_threats=recent_threats,
        notification_count=notification_count
    )