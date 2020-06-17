from application import db
from datetime import datetime

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(10), nullable = False)
    surname = db.Column(db.String(50), nullable = False)
    students = db.relationship('Classrooms')
    
    def __repr__(self):
        return ''.join([
            'Teacher ID: ', self.id, '\r\n',
            'Title: ', self.title, '\r\n',
            'Name: ', self.surname, '\r\n'
        ])

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

class Classrooms(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    subject = db.Column(db.String(50), nullable = False)
    students = db.relationship('Students')

    def __repr__(self):
        return ''.join([
            'Classroom ID: ', self.id, '\r\n',
            'Teacher ID: ', self.teacher_id, '\r\n',
            'Student ID: ', self.teacher_id, '\r\n',
            'Class Size: ', self.class_size, '\r\n'
        ])
