from flask import Flask,render_template,url_for,send_from_directory
import os

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/')
def home():
    return render_template('home.html', title='Home')
@app.route('/about')
def about():
    return render_template('about.html', title='About')
@app.route('/donate')
def donate():
    return render_template('donate.html', title='Donate')
@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

app.run(host='0.0.0.0', port=81)
