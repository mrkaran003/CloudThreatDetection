from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from models.models import User
from utils.database import db

auth = Blueprint("auth", __name__)

# ==========================================
# Login
# ==========================================

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        print("Username entered:", username)
        print("Password entered:", password)
        print("User found:", user)

        if user:
            print("Database password:", user.password)

        if user and user.password == password:

            login_user(user)

            flash("Login Successful!", "success")

            return redirect(url_for("dashboard.home"))

        flash("Invalid Username or Password", "danger")

    return render_template("login.html")


# ==========================================
# Register
# ==========================================

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(
            username=username
        ).first()

        if existing_user:

            flash(
                "Username already exists.",
                "warning"
            )

            return redirect(
                url_for("auth.register")
            )

        existing_email = User.query.filter_by(
            email=email
        ).first()

        if existing_email:

            flash(
                "Email already registered.",
                "warning"
            )

            return redirect(
                url_for("auth.register")
            )

        new_user = User(

            fullname=fullname,

            username=username,

            email=email,

            password=password,

            role="User"
        )

        db.session.add(new_user)

        db.session.commit()

        flash(
            "Registration Successful! Please login.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html"
    )


# ==========================================
# Logout
# ==========================================

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Logged out successfully.",
        "info"
    )

    return redirect(
        url_for("auth.login")
    )