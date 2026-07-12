from flask import Blueprint, render_template
from flask_login import login_required

from models.models import UploadedFile, ThreatLog

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/")
@login_required
def home():

    total_files = UploadedFile.query.count()

    total_threats = ThreatLog.query.count()

    high_risk = ThreatLog.query.filter_by(
        severity="High"
    ).count()

    return render_template(
        "dashboard.html",
        total_files=total_files,
        total_threats=total_threats,
        high_risk=high_risk
    )