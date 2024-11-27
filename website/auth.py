from flask import Blueprint, render_template, request,flash

auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET', 'POST'])
def login():

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords must match", category="error")
        elif len(password1) <7:
            flash("Password must be at least 7 characters", category="error")
        else:
            flash("You have successfully registered!", category="success")

    return render_template("register.html")