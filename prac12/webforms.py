from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length, Email

#Create a search form
class SearchForm(FlaskForm):
    search = StringField("Search...", validators = [DataRequired()])
    submit = SubmitField("Submit")
    
#Create a login Form    
class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min = 5)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 5)])
    submit = SubmitField("Submit")