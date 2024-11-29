from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Please enter a note', category='error')
        else:
            new_note = Note(date=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Your note has been saved', category='success')

    return render_template("home.html",user=current_user)