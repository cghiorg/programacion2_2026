from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

productos = [
    {"nombre": "Mouse", "precio": 8000, "stock": 15},
    {"nombre": "Teclado", "precio": 12000, "stock": 8},
    {"nombre": "Monitor", "precio": 95000, "stock": 4}
]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/productos", methods=["GET", "POST"])
def productos_view():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }

        productos.append(nuevo_producto)

        return redirect(url_for("productos_view"))

    return render_template("productos.html", productos=productos)


if __name__ == "__main__":
    app.run(debug=True)