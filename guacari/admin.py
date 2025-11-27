from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .utils.decorators import admin_required, login_required
from .models import Post, Evento
from .extensions import db
from datetime import datetime

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
@admin_required
def dashboard():
    return render_template("admin_dashboard.html")

@admin_bp.route("/posts/nuevo", methods=["GET", "POST"])
@admin_required
def new_post():
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        contenido = request.form["contenido"].strip()
        if not titulo or not contenido:
            flash("Todos los campos son requeridos.", "warning")
            return redirect(url_for("admin.new_post"))
        p = Post(titulo=titulo, contenido=contenido)
        db.session.add(p)
        db.session.commit()
        flash("Post creado.", "success")
        return redirect(url_for("main.index"))
    return render_template("admin_new_post.html")

@admin_bp.route("/eventos/nuevo", methods=["GET", "POST"])
@admin_required
def new_event():
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        descripcion = request.form["descripcion"].strip()
        fecha_str = request.form["fecha_evento"].strip()
        if not titulo or not descripcion or not fecha_str:
            flash("Todos los campos son requeridos.", "warning")
            return redirect(url_for("admin.new_event"))
        fecha_evento = datetime.fromisoformat(fecha_str)  # espera 'YYYY-MM-DDTHH:MM' o 'YYYY-MM-DD'
        ev = Evento(titulo=titulo, descripcion=descripcion, fecha_evento=fecha_evento, creado_por=session.get("user_id"))
        db.session.add(ev)
        db.session.commit()
        flash("Evento creado.", "success")
        return redirect(url_for("main.eventos"))
    return render_template("admin_new_event.html")
