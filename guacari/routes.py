from flask import Blueprint, render_template
from .models import Post, Evento

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    posts = Post.query.order_by(Post.fecha.desc()).all()
    return render_template("index.html", posts=posts)

@main_bp.route("/post/<int:id>")
def post(id):
    p = Post.query.get_or_404(id)
    return render_template("post.html", post=p)

@main_bp.route("/eventos")
def eventos():
    evs = Evento.query.order_by(Evento.fecha_evento).all()
    return render_template("eventos.html", eventos=evs)

@main_bp.route("/eventos/<int:id>")
def evento_detalle(id):
    evento = Evento.query.get_or_404(id)
    return render_template("event_detail.html", evento=evento)

