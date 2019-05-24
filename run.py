import os
from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
from plugins import * 

UPLOAD_FOLDER = './templates/uploads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__, static_folder='templates/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
# @app.route('/')
# def welcome():
#     return redirect('/login')

@app.route('/upfile', methods=['GET', 'POST'])
def upload_file():
    error = None
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # os.remove('templates/img/res.png')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = app.config['UPLOAD_FOLDER'] + '/' + filename
            upload_res = []
            with open(filepath, 'r') as f:
                for line in f.readlines():
                    temp_list_attr = line.split('\t')
                    FULL_SET.append(Human(
                        temp_list_attr[0],
                        int(temp_list_attr[2]),
                        int(temp_list_attr[3]),
                        temp_list_attr[1].strip()
                    ).get_fuzzy_info())
                f.close()
                upload_res = boosting2('a').values()
            shape, num = getIndex(upload_res)
            os.remove(filepath)
            return render_template('res.html', error=error, shape=shape, num_res=num)
    return redirect(url_for('/')) 
 
@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST':
        h = request.form['height'] 
        w = request.form['weight']
        g = request.form['gender']
        hum = Human("a", int(h), int(w), g)
        FULL_SET.append(hum.get_fuzzy_info())
        res = boosting()
        return res
    return redirect(url_for('/'))
 
 
# Route for handling the login page logic
@app.route('/', methods=['GET'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('index.html', error=error)
 
 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)