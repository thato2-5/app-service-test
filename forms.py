from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email

# Create a Registration form
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    email1 = StringField("Confirm Email", validators = [DataRequired(), Email(), EqualTo('email', message = "Emails must Match!")])
    password = PasswordField("Password", validators = [DataRequired(), Length(min = 5)])
    password1 = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign up")
    
# Create a Login Form
class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired(), Length(min = 5)])
    submit = SubmitField("Login")