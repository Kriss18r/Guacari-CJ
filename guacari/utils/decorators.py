from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("user_id"):
            flash("Debes iniciar sesión para acceder.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get("role") != "admin":
            flash("No tienes permisos para acceder a esta sección.", "danger")
            return redirect(url_for("main.index"))
        return f(*args, **kwargs)
    return decorated
