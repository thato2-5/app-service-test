from flask import Flask, flash, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Create the app instance
app = Flask(__name__)

# Create the app configurations
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///todo.db'
app.config["SECRET_KEY"] = "DeploymentTest"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the database instance
db = SQLAlchemy(app)

# Create the models
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    
    def __init__(self, content):
        self.content = content
    
    # Readable string representation    
    def __repr__(self):
        return f'<Task {self.id}: {self.done}>'
    
# Create the Task table
with app.app_context():
    # Delete existing table
    # db.drop_all()
    db.create_all()
    
# Create the routes

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)
    
@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        flash('Please enter text for your task')
        return redirect('/')
    task = Task(content)
    # Prepare write operation
    db.session.add(task)
    # Perform write operation
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    # Prepare delete opeartion
    db.session.delete(task)
    # Perform delete operation
    db.session.commit()
    return redirect('/')

@app.route('/edit', methods=['POST'])
def edit_task():
    task_id = request.form['task_id']
    edit_text = request.form['edit_text']
    if not edit_text:
        flash('Please enter text for your task')
        return redirect('/')
    task = Task.query.get(task_id)
    # task = Task.query.filter_by(id = task_id).first()
    # task = Task.query.filter_by(id = task_id).all()
    task.content = edit_text
    # Perform update operation
    db.session.commit()
    return redirect('/')

@app.route('/finished')
def resolve_tasks():
    tasks = Task.query.all()
    for task in tasks:
        if not task:
            return redirect('/')
        if not task.done:
            task.done = True
    # Perform update operation
    # db.session.rollback()
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)