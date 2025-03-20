from flask_wtf import FlaskForm #type: ignore
from wtforms import StringField, PasswordField, SubmitField#type: ignore
from wtforms.validators import DataRequired#type: ignore

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

