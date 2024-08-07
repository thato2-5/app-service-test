from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup/', methods=['POST'])
def signUp():
    name = None
    if request.method == 'POST':
        name = request.form.get('username')
    return '<h3>Success, button pressed {name}!</h3>'.format(name=name)

if __name__ == '__main__':
    app.run(debug=True)
