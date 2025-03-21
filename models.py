from flask_sqlalchemy import SQLAlchemy #type: ignore
import datetime
from flask_login import UserMixin #type: ignore
from werkzeug.security import generate_password_hash, check_password_hash #type: ignore

db = SQLAlchemy()  

class Alumnos(db.Model): 
    __tablename__ = 'alumno'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido_paterno = db.Column(db.String(50))
    apellido_materno = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.Date, default=datetime.datetime.now, server_default=db.func.now())
    grupo = db.Column(db.String(10))
    respuestas = db.relationship('Respuesta', backref='alumno', lazy=True)

class Pregunta(db.Model):
    __tablename__ = 'pregunta'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500))
    opcion_a = db.Column(db.String(200))
    opcion_b = db.Column(db.String(200))
    opcion_c = db.Column(db.String(200))
    opcion_d = db.Column(db.String(200))
    respuesta_correcta = db.Column(db.String(1), nullable=False)
    respuestas = db.relationship('Respuesta', backref='pregunta', lazy=True)    
    
class Respuesta(db.Model):
    __tablename__ = 'respuesta'
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumno.id'), nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'), nullable=False)
    respuesta_elegida = db.Column(db.String(1), nullable=False)
    
class Calificacion(db.Model):
    __tablename__ = 'calificacion'
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumno.id'), nullable=False)
    calificacion = db.Column(db.Float, nullable=False)



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


