from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    edad = request.form.get("edad")
    carrera = request.form.get("carrera")
    email = request.form.get("email")

    if not nombre or not apellido or not edad or not carrera or not email:
        return render_template(
            "index.html",
            error="Todos los campos son obligatorios."
        )

    return render_template(
        "resultado.html",
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        carrera=carrera,
        email=email
    )


if __name__ == "__main__":
    app.run(debug=True)