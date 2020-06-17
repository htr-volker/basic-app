from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, FloatField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application import db

class AddTeacher(FlaskForm):
    title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min = 1, max = 10)
            ])
    surname = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min = 3, max = 50)
            ])
    submit = SubmitField('Add Teacher')

class AddStudent(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min = 3, max = 50)
            ])
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min = 3, max = 50)
            ])
    teacher_one = StringField('Teacher 1\'s Last Name',
            validators = [
                Length(max = 50)
            ])
    teacher_two = StringField('Teacher 2\'s Last Name',
            validators = [
                Length(max = 50)
            ])
    subject = StringField('Subject',
            validators = [
                Length(max = 50)
            ])
    submit = SubmitField('Add Student')
