from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mibase.db'

db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float)
    
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    
    
with app.app_context():

    producto = Producto(nombre="Teclado",precio=5000)
    cliente = Cliente(nombre="Carlos",direccion="Aca") 
    
    db.session.add(cliente)   
    db.session.add(producto)
    
    db.session.commit() 
    
    db.create_all()