from flask import Flask, render_template

app = Flask(__name__)

estudiantes = [
    {
        "id": 1,
        "nombre": "Ana Pérez",
        "edad": 21,
        "carrera": "Ciencia de Datos",
        "estado": "Activo"
    },
    {
        "id": 2,
        "nombre": "Luis Gómez",
        "edad": 24,
        "carrera": "Inteligencia Artificial",
        "estado": "Activo"
    },
    {
        "id": 3,
        "nombre": "María Díaz",
        "edad": 20,
        "carrera": "Desarrollo Web",
        "estado": "Inactivo"
    },
    {
        "id": 4,
        "nombre": "Juan Perez",
        "edad": 26,
        "carrera": "Inteligencia Artificial",
        "estado": "Activo"
    }
]


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/estudiantes")
def listar_estudiantes():
    return render_template(
        "estudiantes.html",
        estudiantes=estudiantes
    )


@app.route("/estudiante/<int:id>")
def detalle_estudiante(id):
    estudiante_encontrado = None

    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiante_encontrado = estudiante

    return render_template(
        "detalle.html",
        estudiante=estudiante_encontrado
    )

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

if __name__ == "__main__":
    app.run(debug=True)