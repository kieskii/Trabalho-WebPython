from flask import render_template, url_for, flash, redirect, request
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, TaskForm
from app.models import User, Task
from flask_login import login_user, current_user, logout_user, login_required
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login failed. Please check your email and password.', 'danger')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', tasks=tasks)

@main.route('/tasks/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        # Define o assigned_user_id como None se o valor for vazio
        assigned_user_id = form.assigned_user.data if form.assigned_user.data else None
        task = Task(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data,
            author=current_user,
            assigned_user_id=assigned_user_id  # Atribui o usuário ou None
        )
        db.session.add(task)
        db.session.commit()
        flash('Your task has been created!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('tasks.html', form=form, legend='New Task')


@main.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm()

    if request.method == 'GET':
        form.task_id.data = task.id
        form.title.data = task.title
        form.description.data = task.description
        form.status.data = task.status
        form.assigned_user.data = task.assigned_user_id if task.assigned_user_id else ""
    
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.status = form.status.data
        # Define o assigned_user_id como None se o valor for vazio
        task.assigned_user_id = form.assigned_user.data if form.assigned_user.data else None
        db.session.commit()
        flash('Sua tarefa foi atualizada!', 'success')
        return redirect(url_for('main.dashboard'))
    
    return render_template('tasks.html', form=form, legend='Editar Tarefa')




@main.route('/tasks/delete/<int:task_id>', methods=['GET', 'POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Sua tarefa foi deletada!', 'success')
    return redirect(url_for('main.dashboard'))

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
