from flask import Blueprint, render_template, redirect, url_for
from .forms import RegistrationForm, LoginForm
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logic for user authentication
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Login', form=form)
