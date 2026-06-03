from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyectos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    area = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    integrantes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Proyecto {self.titulo}>'


@app.route('/')
def index():
    proyectos = Proyecto.query.all()
    return render_template('index.html', proyectos=proyectos)


@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        area = request.form['area']
        estado = request.form['estado']
        integrantes = request.form['integrantes']

        proyecto = Proyecto(
            titulo=titulo,
            descripcion=descripcion,
            area=area,
            estado=estado,
            integrantes=integrantes
        )

        db.session.add(proyecto)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('formulario.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    proyecto = Proyecto.query.get_or_404(id)

    if request.method == 'POST':
        proyecto.titulo = request.form['titulo']
        proyecto.descripcion = request.form['descripcion']
        proyecto.area = request.form['area']
        proyecto.estado = request.form['estado']
        proyecto.integrantes = request.form['integrantes']

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('editar.html', proyecto=proyecto)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    proyecto = Proyecto.query.get_or_404(id)

    db.session.delete(proyecto)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)