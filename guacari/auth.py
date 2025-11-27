from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import User
from .extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Usuario y contraseña requeridos.", "warning")
            return redirect(url_for("auth.register"))

        # verificar usuario existente
        existing = User.query.filter_by(username=username).first()
        if existing:
            flash("Este usuario ya existe.", "danger")
            return redirect(url_for("auth.register"))

        # crear usuario
        user = User(username=username)
        user.set_password(password)

        # IMPORTANTE: hacer al primer usuario administrador
        if User.query.count() == 0:
            user.role = "admin"

        db.session.add(user)
        db.session.commit()

        flash("Usuario creado correctamente. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session.clear()
            session["user_id"] = user.id
            session["username"] = user.username
            session["role"] = user.role
            flash("Has iniciado sesión.", "success")
            return redirect(url_for("main.index"))
        flash("Usuario o contraseña incorrectos.", "danger")
        return redirect(url_for("auth.login"))
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Has cerrado sesión.", "info")
    return redirect(url_for("main.index"))
