from flask import Flask, render_template, redirect, url_for, flash #type: ignore
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user #type: ignore
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

users = {
    'admin': {'password': 'admin123'},
    'user': {'password': 'user123'},
    'alonso': {'password': 'alonso123'}
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username)
    return None

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.id)


@app.route('/sito')
@login_required
def sito():
    return render_template('sito.html', username=current_user.id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)