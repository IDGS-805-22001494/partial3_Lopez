from flask import Flask,render_template,request,redirect,url_for,flash #type:ignore
from flask_wtf import FlaskForm #type:ignore
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user #type: ignore

import forms
from models import db, Alumnos, Pregunta, Respuesta, Calificacion, User   #type:ignore
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect #type:ignore
from datetime import datetime
from forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash #type: ignore

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flask_exam'
app.config['SECRET_KEY'] = '1233455'
db.init_app(app)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

# users = {
#     'admin': {'password': 'admin123'},
#     'user': {'password': 'user123'},
#     'alonso': {'password': 'alonso123'}
# }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# @app.errorhandler(400)
# def page_not_found(e):
#     return render_template('400.html'), 400

def calcular_calificacion(alumno_id):
    respuestas_alumno = db.session.query(Respuesta).filter_by(alumno_id=alumno_id).all()

    if not respuestas_alumno:
        return None

    total_preguntas = len(respuestas_alumno)
    respuestas_correctas = 0

    for respuesta in respuestas_alumno:
        pregunta = db.session.query(Pregunta).filter_by(id=respuesta.pregunta_id).first()
        if pregunta:
            if respuesta.respuesta_elegida == pregunta.respuesta_correcta:
                respuestas_correctas += 1

    calificacion_final = (respuestas_correctas / total_preguntas) * 10

    calificacion_existente = db.session.query(Calificacion).filter_by(alumno_id=alumno_id).first()
    
    if calificacion_existente:
        calificacion_existente.calificacion = calificacion_final
    else:
        nueva_calificacion = Calificacion(alumno_id=alumno_id, calificacion=calificacion_final)
        db.session.add(nueva_calificacion)

    db.session.commit()
    return calificacion_final



@app.route('/')

def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    
    return render_template('login.html', form=form)
# @app.errorhandler(404)
# @login_required
# def page_not_found(e):
#     return render_template('404.html'), 404



@app.route('/alumnos', methods=['GET', 'POST'])
@login_required

def alumnos():
    create_form = forms.UserForm(request.form)  
    if request.method == 'POST':
        alumno = Alumnos(
            nombre=create_form.nombre.data,
            apellido_paterno=create_form.apellido_paterno.data,
            apellido_materno=create_form.apellido_materno.data,
            fecha_nacimiento=create_form.fecha_nacimiento.data,
            grupo=create_form.grupo.data
        )
        db.session.add(alumno)
        db.session.commit()
        flash('Alumno agregado con éxito', 'success')
        return redirect(url_for('alumnos'))
    elif request.method == 'POST' and not create_form.validate():
        flash('Error al registrar alumno', 'error')
    return render_template('alumnos.html', form=create_form)


@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        if User.query.filter_by(username=username).first():
            flash('El nombre de usuario ya está en uso', 'danger')
        else:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/preguntas', methods=['GET', 'POST'])
@login_required

def preguntas():
    create_form =forms.UserForm2(request.form)
    if request.method=='POST':
        pregunta = Pregunta(
            texto=create_form.texto.data,
            opcion_a=create_form.opcion_a.data,
            opcion_b=create_form.opcion_b.data,
            opcion_c=create_form.opcion_c.data,
            opcion_d=create_form.opcion_d.data,
            respuesta_correcta=create_form.respuesta_correcta.data
        )
        db.session.add(pregunta)
        db.session.commit()
        flash('Pregunta agregada con éxito', 'success') 
        return redirect(url_for('preguntas'))
    elif request.method == 'POST' and not create_form.validate():
        flash('Error en el formulario. Revise los datos.', 'error')  
    return render_template('preguntas.html', form=create_form)


def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

@app.route('/examen', methods=['GET', 'POST'])
@login_required

def examen():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido_paterno']
        alumno = Alumnos.query.filter_by(nombre=nombre, apellido_paterno=apellido_paterno).first()
        if alumno:
            preguntas = Pregunta.query.all()
            edad = calcular_edad(alumno.fecha_nacimiento)
            return render_template('examen.html', alumno=alumno, preguntas=preguntas, edad=edad)
        else:
            flash('Alumno no encontrado', 'danger')
    return render_template('examen.html')

@app.route('/guardar_respuestas', methods=['POST'])
@login_required

def guardar_respuestas():
    alumno_id = request.form.get('alumno_id')
    if not alumno_id:
        flash('Error: Alumno no identificado', 'danger')
        return redirect(url_for('examen'))

    preguntas = Pregunta.query.all()
    total_preguntas = len(preguntas)
    respuestas_correctas = 0

    for pregunta in preguntas:
        respuesta_elegida = request.form.get(f'p{pregunta.id}')
        if respuesta_elegida:
            es_correcta = respuesta_elegida == pregunta.respuesta_correcta
            if es_correcta:
                respuestas_correctas += 1
            
            respuesta = Respuesta(
                alumno_id=alumno_id,
                pregunta_id=pregunta.id,
                respuesta_elegida=respuesta_elegida
            )
            db.session.add(respuesta)

    calificacion = (respuestas_correctas / total_preguntas) * 100

    nueva_calificacion = Calificacion(
        alumno_id=alumno_id,
        calificacion=calificacion
    )
    db.session.add(nueva_calificacion)
    db.session.commit()

    flash(f'Respuestas guardadas con éxito. Calificación: {calificacion:.2f}', 'success')
    return redirect(url_for('calificaciones'))

@app.route('/calificaciones', methods=['GET', 'POST'])
@login_required

def calificaciones():
    grupos = db.session.query(Alumnos.grupo).distinct().all()
    grupo_seleccionado = None
    alumnos_con_calificaciones = []

    if request.method == 'POST':
        grupo_seleccionado = request.form.get('grupo')
        if grupo_seleccionado:
            alumnos = db.session.query(Alumnos).filter_by(grupo=grupo_seleccionado).all()
            
            for alumno in alumnos:
                calificacion = calcular_calificacion(alumno.id)
                alumnos_con_calificaciones.append((alumno, calificacion))

    return render_template(
        'calificaciones.html',
        grupos=grupos,
        grupo_seleccionado=grupo_seleccionado,
        alumnos_con_calificaciones=alumnos_con_calificaciones
    )



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()  
        db.create_all() 

        
        if not User.query.filter_by(username='admin').first():
            user = User(username='admin')
            user.set_password('admin123')
            db.session.add(user)
            db.session.commit()

    app.run(debug=True)
    
    