from flask import Blueprint, render_template, request,flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
            else:
                flash('Wrong password!', category='error')
        else:
            flash('User not found!', category='error')


    return render_template("login.html")

@auth.route('/logout')
def logout():

    return "<p>Logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered!', category='error')

        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords must match", category="error")
        elif len(password1) <7:
            flash("Password must be at least 7 characters", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            flash("You have successfully registered!", category="success")
            return redirect(url_for('views.home'))

    return render_template("register.html")