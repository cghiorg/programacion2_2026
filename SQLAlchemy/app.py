from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'

db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)

with app.app_context():

    db.create_all()

    produ = Producto.query.get(1)

    # Verificamos si existe
    if produ:
        
        # Eliminar el objeto
        db.session.delete(produ)

        # Confirmar cambios
        db.session.commit()

        print("Producto eliminado correctamente")

    else:
        print("No se encontró el producto")