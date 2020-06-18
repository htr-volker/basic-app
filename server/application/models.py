from application import db
from datetime import datetime

class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return ''.join([
            'Student ID: ', self.id, '\r\n',
            'First Name: ', self.first_name, '\r\n',
            'Last Name: ', self.last_name, '\r\n'
        ])

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(10), nullable = False)
    surname = db.Column(db.String(50), nullable = False)
    classrooms = db.relationship('Students', 
            secondary = 'classrooms', 
            cascade = 'delete', 
            backref = db.backref('classrooms'), 
            lazy = 'dynamic')
    
    def __repr__(self):
        return ''.join([
            'Teacher ID: ', self.id, '\r\n',
            'Title: ', self.title, '\r\n',
            'Name: ', self.surname, '\r\n'
        ])

classrooms = db.Table('classrooms', db.Model.metadata,
    db.Column('teacher_ID', db.Integer, db.ForeignKey('teachers.id')),
    db.Column('student_ID', db.Integer, db.ForeignKey('students.id'))
)
