from flask import Flask, render_template, request, redirect, url_for, flash
from database import session, User  

app = Flask(__name__)
app.secret_key = 'minesecretkey'
#database 
from database import session, User


@app.route('/')
def index():
    return render_template('index.html', total_points=total_points)

@app.route('/academics')
def academics():
    return render_template('academics.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

#for todo list
total_points = 0
tasks = session.query(User).all()

@app.route('/todo')
def todo():
    tasks = session.query(User).all()
    msg = flash('')
    return render_template('todo.html', tasks=tasks, message = msg, total_points=total_points)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    
    if title:
        # Create a new User instance and add it to the database
        new_user = User(task=title, points=10) 
        session.add(new_user)
        session.commit()
        flash("Task added successfully.")
    return redirect(url_for('todo'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    user_to_delete = session.query(User).filter_by(id=task_id).first()

    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print("User deleted successfully.")
    else:
        print("User not found.")
    session.close()
    return redirect(url_for('todo'))

@app.route('/done/<int:task_id>', methods=['POST'])
def update_points(task_id):
    global total_points
    user = session.query(User).filter_by(id=task_id).first()

    if user:
        total_points += user.points
        session.delete(user)
        session.commit()
    else:
        print(f"Invalid task_id: {task_id}")
    session.close()
    return redirect(url_for('todo'))

@app.route('/done/<int:task_id>')
def done_task(task_id):
    update_points(task_id)
    session.close()
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(debug=True)
