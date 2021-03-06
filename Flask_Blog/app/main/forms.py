from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField , PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from .. import db
from ..models.users import User, Role, Society

EqualTo('confirm', message='Passwords must match')

class SignUp(FlaskForm):

    username = StringField('Username: ' , validators= [Length(3,50), DataRequired()])
    email = StringField('Email: ', validators= [Email()])
    password = PasswordField('Password: ' ,validators= [Length(3,50), DataRequired()])
    confirm_password = PasswordField('Confirm Password: ' ,validators= [Length(3,50), DataRequired(), EqualTo('password', message='Passwords must match')])
    Submit = SubmitField('Sign Up !')

    def validate_username(self, username):

        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username Already Taken')
    def validate_email(self, email):

        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('Email Already in Use')

class Login(FlaskForm):


    email = StringField('Email: ', validators = [Email()])
    password = PasswordField('Password: ' ,validators= [Length(3,50), DataRequired()])
    remember = BooleanField('Remember Me')
    Submit = SubmitField('Login')

class SignUp_society(FlaskForm):

    username = StringField('Username: ' , validators= [Length(3,50), DataRequired()])
    email = StringField('Email: ', validators= [Email()])
    Secret_key = StringField('Secret Key:', validators = [DataRequired()])
    society_name = StringField('Society Name:', validators = [DataRequired(), Length(1,100)])
    password = PasswordField('Password: ' ,validators= [Length(3,50), DataRequired()])
    confirm_password = PasswordField('Confirm Password: ' ,validators= [Length(3,50), DataRequired(), EqualTo('password', message='Passwords must match')])
    Submit = SubmitField('Sign Up !')
    
    def validate_username(self, username):

        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username Already Taken')
        
    def validate_email(self, email):

        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('Email Already in Use')

    def validate_society_name(self, username):

        society_user = Society.query.filter_by(society_name = society_name.data).first()
        if society_user:
            raise ValidationError('Username Already Taken')
        elif Secret_key.data != society_user.secret_key:
            raise ValidationError('Invalid Secret Key')

            
       



    
    
    
    
