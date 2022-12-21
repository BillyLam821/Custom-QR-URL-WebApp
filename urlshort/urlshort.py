from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import sys, json, os.path
from werkzeug.utils import secure_filename
from urlshort.qr import create_qr

bp = Blueprint('urlshort', __name__, static_folder='static', template_folder='templates')

@bp.route('/')
def home():
    # session.clear()
    return render_template('home.html', codes=session.items()) ###

# route only allow GET request
# GET = type in, POST = form submission
@bp.route('/your-url', methods=['GET','POST'])
def your_url():
    
    if request.method == 'POST':

        urls = {}

        if os.path.exists('urlshort/urls.json'):
            with open('urlshort/urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            flash('* That short name has already been taken. Please select another name. *')
            return redirect(url_for('urlshort.home'))

        # check URL or file 
        if request.form['targetSelect'] == 'webTarget':
            targetName = 'website'
            urls[request.form['code']] = {'url': request.form['url']}
            session[request.form['code']] = {'url': request.form['url']} ###
            new_url = request.base_url + request.form['code']

        elif request.form['targetSelect'] == 'fileTarget':
            targetName = 'file'
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join('urlshort/static/user_files/' + filename))
            urls[request.form['code']] = {'file': filename}
            session[request.form['code']] = {'file': filename} ###
            new_url = request.base_url + filename
        
        # created by user
        with open('urlshort/urls.json', 'w') as url_file:
            json.dump(urls, url_file) # save dict into file
            # session[request.form['code']] = True

        if request.form['appSelect'] == "urlApp":
            return render_template('yourURL.html', appName='URL', targetName=targetName, code=request.form['code'])

        elif request.form['appSelect'] == 'qrApp':

            if request.files['qrLogo']:
                new_qr = create_qr(new_url, request.form['code'], request.form['qrColor'], 
                                    request.form['qrBackColor'], request.files['qrLogo'])
                
            else:
                new_qr = create_qr(new_url, request.form['code'], request.form['qrColor'], 
                                    request.form['qrBackColor'])
                
            urls[request.form['code']]['qr'] = new_qr
            with open('urlshort/urls.json', 'w') as url_file:
                json.dump(urls, url_file)
                # session[request.form['code']] = True
                session[request.form['code']] = {'qr': new_qr} ###
                # session[request.form['code']] = ('qr', new_qr) ###

            return render_template('yourURL.html', appName='QR code', targetName=targetName, code=request.form['code'], new_QR=new_qr)
        
    else: #GET
        return redirect(url_for('urlshort.home'))


@bp.route('/<string:code>')
def redirect_to_url(code):

    if os.path.exists('urlshort/urls.json'):

        with open('urlshort/urls.json') as urls_file:
            urls = json.load(urls_file)

            if code in urls.keys():
                
                if 'qr' in urls[code].keys():
                    return redirect(url_for('static', filename='user_files/qr/' + urls[code]['qr']))

                elif 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])

                else:
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))

    return abort(404)
    
@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@bp.route('/api')
def session_api():
    return jsonify(list(session.items()))