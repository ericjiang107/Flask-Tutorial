# This is the creation with our forms page
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]) # set limitations onto this since we don't something
    # too short/ too long/ etc. That is called using (validators) 
    # validators=[DataRequired(), Length(min=2, max=20)] --> this is checking the input for specific requirements
    # and that we don't want the input to be empty 
    email = StringField('Email', validators=[DataRequired(), Email()])
    # the (Email) import checks for specific email requirements
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    # the (EqualTo) checks if the password entered is equal to the password for confirmation 
    submit = SubmitField('Sign Up')
    # For the SubmitField, all you need is what to call it in the parameters 

# Creating a LoginForm
class LoginForm(FlaskForm):
    # Using email (it's personal preference since some people like logging in with email and others with username)
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    # Don't need confirm_password since we already did that in the RegistrationForm
    remember = BooleanField('Remember Me')
    # remember is a Boolean field (true or false)
    submit = SubmitField('Login')


