from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from utils.database import db

from models.models import UploadedFile

files = Blueprint(
    "files",
    __name__
)


@files.route("/files")
@login_required
def files_page():

    uploaded_files = UploadedFile.query.order_by(
        UploadedFile.upload_time.desc()
    ).all()

    return render_template(
        "files.html",
        uploaded_files=uploaded_files
    )


@files.route("/files/delete/<int:file_id>")
@login_required
def delete_file(file_id):

    file = UploadedFile.query.get_or_404(file_id)

    db.session.delete(file)

    db.session.commit()

    flash(
        "File deleted successfully.",
        "success"
    )

    return redirect(
        url_for("files.files_page")
    )