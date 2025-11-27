# create_admin.py
from guacari import create_app
from guacari.extensions import db
from guacari.models import User

app = create_app()
with app.app_context():
    u = User.query.filter_by(username="KrisAdmin").first()
    if u:
        u.role = 'admin'
        db.session.commit()
        print("Usuario promovido a admin.")
    else:
        print("No se encontró el usuario.")
