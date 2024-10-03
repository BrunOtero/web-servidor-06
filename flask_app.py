from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>/<prontuary>/<institution>')
def identification(name, prontuary, institution):
    return render_template('identification.html', name=name, prontuary=prontuary, institution=institution)

@app.route('/contextorequisicao')
def requisition_context():
    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host_app = request.host
    return render_template('requisitionContext.html', user_agent=user_agent, remote_ip=remote_ip, host_app=host_app)