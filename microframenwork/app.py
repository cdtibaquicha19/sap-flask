from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'Mi_llave_secreta'


# http://localhost:5000/

@app.route('/')
def inicio():
    if 'username' in session:
        return f'el usuario ya  ha hecho loggin : {session["username"]}'
    return 'no ha hecho login '


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'hola saludo : {nombre}'


@app.route('/edad/<int:edad>')
def mostraredad(edad):
    return f' Tu edad es : {edad}'


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)


@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='cristyan'))


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def pagina_no_enncontrada(error):
    return render_template('error404.html', error=error), 404


# REST  SERVICIOS WEB

@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre,
               'metodo_http': request.method}
    return jsonify(valores)
