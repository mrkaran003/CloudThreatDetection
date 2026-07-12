from flask import Blueprint, render_template
from flask_login import login_required

from models.models import UploadedFile, ThreatLog

report = Blueprint("report", __name__)


@report.route("/report")
@login_required
def report_page():

    total_files = UploadedFile.query.count()

    total_threats = ThreatLog.query.count()

    high_risk = ThreatLog.query.filter_by(
        severity="High"
    ).count()

    low_risk = ThreatLog.query.filter_by(
        severity="Low"
    ).count()

    return render_template(
        "report.html",
        total_files=total_files,
        total_threats=total_threats,
        high_risk=high_risk,
        low_risk=low_risk
    )