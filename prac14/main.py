from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'testing'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Set this to the login route

@app.before_request
def before_request():
    # Check if the user is logged in for protected routes
    if not current_user.is_authenticated and request.endpoint in ['protected_route', 'another_protected_route']:    # Adjust the list to include the endpoints of your protected routes
        flash("Please log in to access this page.", "info")
        return redirect(url_for('login'))

# User class representing application's users

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True)
    password = db.Column(db.String(15), unique = True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __str__(self):
        return f'<Users {self.username}>'
    
    def get_id(self):
        return str(self.id)
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    # logic to load user from database
    active_user = User.query.get(int(user_id))
    if not active_user:
        return None
    return active_user

@app.route('/protected/')
@login_required
def protected_route():
    return 'This is a protected route. Only logged-in users can access it.' 

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    # Replace this with your login logic
    if request.method == 'POST':
        username = request.form['username']
        
        user = User.query.filter_by(username = username).first()
        
        if user:
            login_user(user)
            return redirect(url_for('protected_route'))
        else:
            flash("Invalid username or password.")
    return render_template('login.html')
    
@app.route('/logout/')
def logout():
    logout_user()
    return 'Logged out successfully'
    
if __name__ == "__main__":
    app.run(debug = True)