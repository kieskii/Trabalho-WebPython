from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from wtforms.validators import Optional


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

def coerce_user(value):
    if value == "" or value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None

class TaskForm(FlaskForm):
    task_id = HiddenField() 
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    status = SelectField('Status', choices=[('pendente', 'Pendente'), ('em andamento', 'Em Andamento'), ('concluída', 'Concluída')])
    
    # Use a função de coerção personalizada
    assigned_user = SelectField('Atribuir a', coerce=coerce_user, validators=[Optional()])
    submit = SubmitField('Save Task')
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Inclua uma opção vazia no combobox de atribuição de usuário
        self.assigned_user.choices = [("", "--- Nenhum ---")] + [(user.id, user.username) for user in User.query.all()]