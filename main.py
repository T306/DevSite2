import os
from flask import Flask,render_template,url_for,send_from_directory
from flask_flatpages import FlatPages
from datetime import datetime

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'bloglist'
app.config['FLATPAGES_MARKDOWN_EXTENSIONS'] = ['fenced_code', 'codehilite']

flatpages = FlatPages(app)

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
  
@app.route('/')
def home():
  return render_template('pages/home.html', title='Home')
  
@app.route('/about')
def about():
  return render_template('pages/about.html', title='About')
  
@app.route('/donate')
def donate():
  return render_template('pages/donate.html', title='Donate')
  
@app.route('/projects')
def projects():
  return render_template('pages/projects.html', title='Projects')

@app.route('/blogs/<path:path>')
def page(path):
    page = flatpages.get_or_404(path)
    return render_template('pages/blogtemp.html', page=page, title=path)
  
@app.route('/blogs')
def blogs():
  blurbs = [p for p in flatpages if "date" in p.meta]
  sorted_pages=sorted(blurbs, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%b %d %y"))
  return render_template('pages/blogs.html', flatpages=sorted_pages, title='Blogs')
  
                ### Errors ###

@app.errorhandler(404)
def page_not_found(error):
  return render_template('errors/404.html'), 404

app.run(host='0.0.0.0', port=81)