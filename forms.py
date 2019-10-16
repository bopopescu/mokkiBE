from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):  #inherits from FlaskForm
    firstname = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)]) #we use validators which are classes that we import
    lastname = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)]) #we use validators which are classes that we import
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Sign Up')

class SearchForm(FlaskForm):  #inherits from FlaskForm
    search = StringField('Search',
                        validators=[DataRequired()])
    submit = SubmitField('Search')


