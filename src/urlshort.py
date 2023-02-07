from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
from werkzeug.utils import secure_filename
from src.qr import create_qr
from src.database import db, Shorts

bp = Blueprint('urlshort', __name__, static_folder='static', template_folder='templates')

@bp.route('/')
def home():
    # session.clear()
    return render_template('home.html', codes=session) ###

# Subsequence Page for Generator
@bp.route('/your-url', methods=['GET','POST'])
def your_url():

    if request.method == 'POST':

        # check if short name exists
        code = Shorts.query.filter_by(short_name = request.form['code']).first()
        if code:
            flash('* That short name has already been taken. Please select another name. *')
            return redirect(url_for('urlshort.home'))

        # get form variables
        short_name = request.form['code']
        app_name = request.form['appSelect']
        targetName = request.form['targetSelect']
        session[short_name] = {"app": app_name, "target": targetName}

        # handle target (website / file)
        if targetName == 'Website':
            original_url = request.form['url']
            

        elif targetName == 'File':
            file = request.files['file']
            filename = short_name + secure_filename(file.filename)
            file.save('src/static/user_files/' + filename)
            original_url = 'user_files/' + filename

        # set new_QR default value as None
        new_QR = None

        # QR app section
        # short URL redirect to QR code file
        # scanning QR code redirect to original website
        if app_name == 'QR Code Generator':

            qr_logo = request.files['qrLogo']
            if qr_logo.filename == '':
                qr_logo = None
                
            new_QR = create_qr(original_url, short_name, request.form['qrColor'], 
                                request.form['qrBackColor'], qr_logo)

            original_url = 'user_files/qr/' + new_QR

        session[short_name]["original_url"] = original_url

        # add data to db
        shortURL = Shorts(target=targetName, app=app_name, original_url=original_url, short_name=short_name) ###working here
        db.session.add(shortURL)
        db.session.commit()
        return render_template('yourURL.html', appName=app_name, targetName=targetName, code=short_name, new_QR=new_QR)

    else: #GET
        return redirect(url_for('urlshort.home'))


@bp.route('/<string:code>')
def redirect_to_url(code):

    if Shorts.query.filter_by(short_name = code).first():

        fetch_result = Shorts.query.filter_by(short_name = code).first()
        redirect_url = fetch_result.original_url

        if fetch_result.app == 'QR Code Generator' or fetch_result.target == 'File':
            return redirect(url_for('static', filename = redirect_url))
        else:
            return redirect(redirect_url)

    return abort(404)
    

@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@bp.route('/api')
def session_api():
    return jsonify(list(session.items()))