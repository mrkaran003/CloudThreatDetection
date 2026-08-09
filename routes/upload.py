from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app
)

from flask_login import (
    login_required,
    current_user
)

from utils.helper import (
    allowed_file,
    save_file
)

from utils.database import db

from models.models import (
    UploadedFile,
    ThreatLog
)

from models.threat_model import ThreatDetectionEngine


upload = Blueprint(
    "upload",
    __name__
)


@upload.route(
    "/upload",
    methods=["GET", "POST"]
)
@login_required
def upload_file():

    if request.method == "POST":

        if "file" not in request.files:

            flash(
                "Please choose a file.",
                "danger"
            )

            return redirect(
                request.url
            )

        file = request.files["file"]

        if file.filename == "":

            flash(
                "No file selected.",
                "warning"
            )

            return redirect(
                request.url
            )

        if not allowed_file(
            file.filename,
            current_app.config[
                "ALLOWED_EXTENSIONS"
            ]
        ):

            flash(
                "Invalid file type.",
                "danger"
            )

            return redirect(
                request.url
            )

        filename, filepath = save_file(
            file,
            current_app.config[
                "UPLOAD_FOLDER"
            ]
        )

        uploaded = UploadedFile(
            filename=filename,
            uploaded_by=current_user.username,
            file_size=0,
            file_type=filename.rsplit(
                ".",
                1
            )[1],
            status="Analyzing"
        )

        db.session.add(
            uploaded
        )

        db.session.commit()

        engine = ThreatDetectionEngine()

        result = engine.analyze_file(
            filepath
        )

        if result["status"] == "success":

            confidence = result["confidence"]

            if confidence >= 90:
                severity = "Critical"

            elif confidence >= 75:
                severity = "High"

            elif confidence >= 50:
                severity = "Medium"

            else:
                severity = "Low"

            threat = ThreatLog(
                filename=filename,
                threat_type=result["prediction"],
                severity=severity,
                prediction=str(
                    result["prediction"]
                ),
                confidence=confidence,
                remarks="AI Analysis Completed"
            )

            db.session.add(
                threat
            )

            uploaded.status = "Completed"

            db.session.commit()

            flash(
                "AI analysis completed successfully.",
                "success"
            )

        else:

            uploaded.status = "Failed"

            db.session.commit()

            flash(
                result["message"],
                "danger"
            )

        return redirect(
            url_for(
                "dashboard.home"
            )
        )

    return render_template(
        "upload.html"
    )