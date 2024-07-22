from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
login_manager = LoginManager(app)

# User class representing application's users
class User:
    def __init__(self, user_id):
        self.id = user_id
        
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

@login_manager.user_loader
def load_user(user_id):
    # Replace this with your logic to load a user from your database
    return User(user_id)

@app.route('/protected/')
@login_required
def protected_route():
    return 'This is a protected route. Only logged-in users can access it.'

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    # Replace this with your login logic
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        user = User(user_id)
        login_user(user)    # User now logged in
        return redirect(url_for('protected_route'))
    return render_template('login.html')

@app.route('/logout/')
def logout():
    logout_user()
    return 'Logged out successfully'
