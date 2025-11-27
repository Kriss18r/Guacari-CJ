from flask import Blueprint, render_template, request, redirect, url_for
from .models import Post
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.order_by(Post.fecha.desc()).all()
    return render_template('index.html', posts=posts)

@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', post=post)

@main.route('/nuevo', methods=['GET', 'POST'])
def nuevo_post():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']

        nuevo = Post(titulo=titulo, contenido=contenido)
        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('new_post.html')
