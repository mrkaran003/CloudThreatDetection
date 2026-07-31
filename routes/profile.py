from flask import Blueprint, render_template

from flask_login import (
    login_required,
    current_user
)

from models.models import (
    UploadedFile,
    ThreatLog
)

profile = Blueprint(
    "profile",
    __name__
)


@profile.route("/profile")
@login_required
def profile_page():

    total_uploads = UploadedFile.query.filter_by(

        uploaded_by=current_user.username

    ).count()

    total_threats = ThreatLog.query.count()

    high_risk = ThreatLog.query.filter_by(

        severity="High"

    ).count()

    return render_template(

        "profile.html",

        user=current_user,

        total_uploads=total_uploads,

        total_threats=total_threats,

        high_risk=high_risk

    )