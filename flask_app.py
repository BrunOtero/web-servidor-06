from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<username>/<prontuary>/<institution>')
def identification(username, prontuary, institution):
    return render_template('identification.html', username=username, prontuary=prontuary, institution=institution)

@app.route('/contextorequisicao/<username>')
def requisitionContext(username):
    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host_app = request.host
    return render_template('requisitionContext.html', username=username, user_agent=user_agent, remote_ip=remote_ip, host_app=host_app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404