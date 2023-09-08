from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# Flask-App erstellen
app = Flask(__name__)

# Flask-Konfigurationen (z. B. Datenbank-URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://testuser1:Ifa$2023@20.216.164.5/todolistdb'
app.config['SECRET_KEY'] = 'Ifa$2023'

# Datenbank-Initialisierung
db = SQLAlchemy(app)

# Benutzerauthentifizierung initialisieren
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Benutzermodell erstellen
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Routen und Ansichten

# Startseite (zeigt die Login-Seite)
@app.route('/')
def home():
    return redirect(url_for('login'))

# Login-Seite
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Erfolgreich angemeldet.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Ungültige Anmeldeinformationen. Versuchen Sie es erneut.', 'danger')
    return render_template('login.html')

# Registrierungsseite
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Benutzername bereits vergeben. Bitte wählen Sie einen anderen.', 'danger')
        else:
            new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Registrierung erfolgreich. Melden Sie sich jetzt an.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html')

# Index-Seite (nur für angemeldete Benutzer)
@app.route('/index')
@login_required
def index():
    # Hier kannst du die Aufgabenliste und Anzeigelogik implementieren
    return render_template('index.html')

# Logout-Funktion
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)