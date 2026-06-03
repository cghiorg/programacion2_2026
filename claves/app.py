from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "clave_secreta"

# Usuario de ejemplo
usuario_correcto = "politecnico"

# Contraseña cifrada
password_hash = generate_password_hash("malvinas")


@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        usuario = request.form['usuario']
        password = request.form['password']

        if usuario == usuario_correcto and check_password_hash(password_hash, password):

            session['usuario'] = usuario

            return redirect('/panel')

        else:
            return "Usuario o contraseña incorrectos"

    return render_template('login.html')


@app.route('/panel')
def panel():

    if 'usuario' in session:
        return f"Bienvenido {session['usuario']}"

    return redirect('/')


@app.route('/logout')
def logout():

    session.pop('usuario', None)

    return redirect('/')


app.run(debug=True)