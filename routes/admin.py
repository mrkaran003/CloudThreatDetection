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

from models.models import (
    User,
    UploadedFile,
    ThreatLog
)

admin = Blueprint(
    "admin",
    __name__
)


@admin.route("/admin")
@login_required
def admin_page():

    # Dashboard Statistics
    total_users = User.query.count()

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

    # Recent Users
    recent_users = User.query.order_by(
        User.created_at.desc()
    ).limit(5).all()

    # Recent Uploaded Files
    recent_files = UploadedFile.query.order_by(
        UploadedFile.upload_time.desc()
    ).limit(5).all()

    # All Users
    users = User.query.order_by(
        User.created_at.desc()
    ).all()

    return render_template(

        "admin.html",

        total_users=total_users,

        total_files=total_files,

        total_threats=total_threats,

        critical_risk=critical_risk,

        high_risk=high_risk,

        medium_risk=medium_risk,

        low_risk=low_risk,

        recent_users=recent_users,

        recent_files=recent_files,

        users=users

    )


@admin.route("/admin/role/<int:user_id>")
@login_required
def change_role(user_id):

    user = User.query.get_or_404(user_id)

    if user.id == current_user.id:

        flash(
            "You cannot change your own role.",
            "warning"
        )

        return redirect(
            url_for("admin.admin_page")
        )

    if user.role == "Admin":

        user.role = "User"

    else:

        user.role = "Admin"

    db.session.commit()

    flash(
        "User role updated successfully.",
        "success"
    )

    return redirect(
        url_for("admin.admin_page")
    )


@admin.route("/admin/delete/<int:user_id>")
@login_required
def delete_user(user_id):

    if user_id == current_user.id:

        flash(
            "You cannot delete your own account.",
            "danger"
        )

        return redirect(
            url_for("admin.admin_page")
        )

    user = User.query.get_or_404(user_id)

    db.session.delete(user)

    db.session.commit()

    flash(
        "User deleted successfully.",
        "success"
    )

    return redirect(
        url_for("admin.admin_page")
    )