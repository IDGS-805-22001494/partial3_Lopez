from flask_wtf import FlaskForm #type:ignore
from wtforms import StringField, DateField, SelectField, SubmitField #type:ignore
from wtforms.validators import DataRequired, Length #type:ignore
from wtforms import Form, StringField, PasswordField, SubmitField #type:ignore

class UserForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    apellido_materno = StringField('Apellido Materno', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    grupo = StringField('Grupo', validators=[DataRequired()])
    submit = SubmitField('Registrar Alumno')

class UserForm2(Form):
    texto = StringField('Pregunta', validators=[DataRequired()])
    opcion_a = StringField('Opción A', validators=[DataRequired()])
    opcion_b = StringField('Opción B', validators=[DataRequired()])
    opcion_c = StringField('Opción C', validators=[DataRequired()])
    opcion_d = StringField('Opción D', validators=[DataRequired()])
    respuesta_correcta = SelectField('Respuesta Correcta', choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], validators=[DataRequired()])
    submit = SubmitField('Agregar Pregunta')
    
    
class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=50)])
    submit = SubmitField('Registrarse')
