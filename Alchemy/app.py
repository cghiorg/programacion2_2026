from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///productos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
    

productos = Producto.query.all()

producto = Producto.query.get(1)

productos = Producto.query.filter(
    Producto.precio > 50000
).all()

producto = Producto.query.filter_by(
    nombre="Mouse Gamer"
).first()

productos = Producto.query.order_by(
    Producto.nombre
).all()

productos = Producto.query.order_by(
    desc(Producto.precio)
).all()

productos = Producto.query.limit(3).all()

cantidad = Producto.query.count()

productos = Producto.query.filter(
    Producto.precio > 10000
).order_by(
    Producto.nombre
).all()

