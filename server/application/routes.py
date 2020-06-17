'''
Python file that handles hyperlink routing within the site
'''
from application import app, db
from flask import render_template, redirect, url_for, request
from application.models import Students, Teachers, Classrooms
from application.forms import AddTeacher, AddStudent
import requests
from os import getenv

# Route to home page
@app.route('/', methods = ["GET"])
def home():
    machine = getenv("HOSTNAME")
    teachers = Teachers.query.order_by(Teachers.surname).all()
    return render_template('index.html', title = 'Home', machine = machine, teachers = teachers)

@app.route('/add-teacher', methods = ['GET','POST'])
def add_teacher():
    form = AddTeacher()
    if form.validate_on_submit():
        teacher = Teachers(
            title = form.title.data,
            surname = form.surname.data
        )
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('addteacher.html', title = 'Enter Teacher', form = form)

@app.route('/add-student', methods = ['GET','POST'])
def add_student():
    form = AddStudent()
    if form.validate_on_submit():
        student = Students(
            first_name = form.first_name.data,
            last_name = form.last_name.data
        )

        classroom = Classrooms(subject = form.subject.data)
        classroom.students = student
        
        if form.teacher_one.data != '':
            teacher_one = Teachers.query.filter_by(surname = form.teacher_one.data).first()
            if teacher_one:
                teacher_one.students.append(classroom)
        
        if form.teacher_two.data != '':
            teacher_two = Teachers.query.filter_by(surname = form.teacher_two.data).first()
            if teacher_two:
                teacher_two.students.append(classroom)

        
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('addstudent.html', title = 'Enter Student', form = form)
