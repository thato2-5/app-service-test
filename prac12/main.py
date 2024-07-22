from flask import Flask, render_template, flash
from webforms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'testing'

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        flash("Success data received!")
        return render_template('success.html', name = name, password = password)
    else:
        flash("Error, please complete the form correctly!")
        return render_template('login.html', form = form)
    
if __name__ == "__main__":
    app.run(debug = True)
            