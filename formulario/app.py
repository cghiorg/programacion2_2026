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


@app.route("/")
def inicio():
    return redirect(url_for("listar_productos"))


@app.route("/productos")
def listar_productos():
    productos = Producto.query.all()
    return render_template("listado.html", productos=productos)


@app.route("/productos/nuevo", methods=["GET", "POST"])
def crear_producto():
    if request.method == "POST":
        nuevo_producto = Producto(
            nombre=request.form["nombre"],
            descripcion=request.form["descripcion"],
            precio=float(request.form["precio"]),
            stock=int(request.form["stock"])
        )

        db.session.add(nuevo_producto)
        db.session.commit()

        return redirect(url_for("listar_productos"))

    return render_template("formulario.html", producto=None)


@app.route("/productos/editar/<int:id>", methods=["GET", "POST"])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)

    if request.method == "POST":
        producto.nombre = request.form["nombre"]
        producto.descripcion = request.form["descripcion"]
        producto.precio = float(request.form["precio"])
        producto.stock = int(request.form["stock"])

        db.session.commit()

        return redirect(url_for("listar_productos"))

    return render_template("formulario.html", producto=producto)


@app.route("/productos/eliminar/<int:id>", methods=["POST"])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for("listar_productos"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)