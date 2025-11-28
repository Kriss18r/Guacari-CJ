# create_admin.py
from guacari import create_app
from guacari.extensions import db
from guacari.models import User

app = create_app()
with app.app_context():
    u = User.query.filter_by(username="Lucho").first()
    if u :
        if u.role != 'admin':
            u.role = 'admin'
            db.session.commit()
            print("Usuario promovido a admin.")
        else:
            print("El usuario ya es admin.")
    else:
        print("No se encontró el usuario.")
