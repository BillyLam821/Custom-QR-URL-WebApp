from flask import render_template, redirect, url_for, flash, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from src.auth_forms import LoginForm, RegisterForm
from src.database import db, User

bp = Blueprint('auth', __name__, static_folder='static', template_folder='templates', url_prefix="/auth")

@bp.route('/', methods=['GET','POST'])
def home():

    signForm = LoginForm()
    regForm = RegisterForm()

    # sign in
    if signForm.validate_on_submit():
        user = User.query.filter_by(username=signForm.username.data).first()
        if user:
            if check_password_hash(user.password, signForm.password.data):
                login_user(user)
                print("validated")
                return redirect(url_for('urlshort.home'))
            else:
                print("incorrect pw")
                return redirect(url_for('urlshort.home'))
        else:
            print("user not exists")
            flash('User not exists')
            return render_template('auth.html', signForm=signForm, regForm=regForm) 

    # register
    if regForm.validate_on_submit():
        hashed_password = generate_password_hash(regForm.password.data)
        new_user = User(username=regForm.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('urlshort.home'))

    return render_template('auth.html', signForm=signForm, regForm=regForm) 

@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home'))
