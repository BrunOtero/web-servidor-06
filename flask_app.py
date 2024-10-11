from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<username>')
def hello_user(username):
    return render_template('index.html', username=username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404