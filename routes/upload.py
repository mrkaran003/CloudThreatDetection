from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from datetime import datetime
import os

from models.models import UploadedFile

upload = Blueprint("upload", __name__)

UPLOAD_FOLDER = "uploads"

@upload.route("/upload", methods=["GET", "POST"])
@login_required
def upload_file():

    if request.method == "POST":

        file = request.files.get("file")

        if not file or file.filename == "":
            flash("Please select a file.", "danger")
            return redirect("/upload")

        filename = secure_filename(file.filename)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        filepath = os.path.join(UPLOAD_FOLDER, filename)

        file.save(filepath)

        uploaded = UploadedFile(
            filename=filename,
            uploaded_by=current_user.id,
            uploaded_at=datetime.now()
        )

        uploaded.save()

        flash("File uploaded successfully.", "success")

        return redirect("/files")

    return render_template("upload.html")