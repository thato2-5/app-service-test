from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from forms import RegistrationForm, LoginForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'testing'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class Users(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(20), unique = True)
    email = db.Column(db.String(25), unique = True)
    password = db.Column(db.String(15))
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def __str__(self):
        return f'<User {self.username}>'
    
    def get_id(self):
        return str(self.id)
    
    def is_active(self):
        return True
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    # logic to load user from database
    active_user = Users.query.get(int(user_id))
    if not active_user:
        return None
    return active_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products/')
@login_required
def products():
    return render_template('products.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/settings/')
@login_required
def settings():
    return render_template('settings.html')

@app.route('/signup/', methods = ['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Enter the data into a database
        username = form.username.data
        password = form.password.data
        email = form.email.data
        user = Users(username, email, password)
        try:
            db.session.add(user)
            db.session.commit()
            flash ( {username} +" was successfully added")
        except IntegrityError:
            db.session.rollback()
            flash("Error: Username or Email or Password already exists inthe database")
            return render_template('login.html', form = form)
        return render_template('login.html', form = form)
    return render_template('signup.html', form = form)

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        active_user = Users.query.filter_by(username = username, password = password).first()
        if not active_user:
            flash("Error, User not available")
            return render_template('login.html', form = form)
        else:
            login_user(active_user)
            return render_template('index.html', form = form)
    return render_template('login.html', form = form)

if __name__ == "__main__":
    app.run(debug = True)