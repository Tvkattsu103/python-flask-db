from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    users = [
        {'id': 'u01','name':'Tuan'},
        {'id': 'u02','name':'Nhat'},
        {'id': 'u03','name':'Nguyet'}
        ]
    return render_template('index.html', users=users)