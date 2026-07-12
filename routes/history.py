from flask import Blueprint, render_template
from flask_login import login_required

from models.models import ThreatLog

history = Blueprint("history", __name__)


@history.route("/history")
@login_required
def history_page():

    threats = ThreatLog.query.order_by(
        ThreatLog.detected_at.desc()
    ).all()

    return render_template(
        "history.html",
        threats=threats
    )