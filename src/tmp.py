
@auth.route('/', methods=['GET','POST'])
def home():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if auth.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('auth.html'), form=form)

    return render_template('auth.html', form=form) 


@auth.route('/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = auth.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.html'), regForm=form)

    return render_template('auth.html', regForm=form)