from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
  first_name = StringField('Informe o seu nome', validators= [DataRequired()])
  last_name = StringField('Informe o seu sobrenome:', validators=[DataRequired()])
  institution = StringField('Informe a sua Insituição de ensino:', validators=[DataRequired()])
  subject = SelectField('Informe a sua disciplina:', choices=['DSWA5', 'DWBA4', 'Gestão de projetos'], validators=[DataRequired()])
  submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY_S3CR37_K3Y'

moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    remote_ip = request.remote_addr
    application_host = request.host
    form = UserForm()

    if form.validate_on_submit():
        full_name = form.first_name.data + ' ' + form.last_name.data
        session['name'] = full_name
        session['institution'] = form.institution.data
        session['subject'] = form.subject.data

        form.first_name.data = ''
        form.last_name.data = ''
        form.institution.data = ''
        form.subject.data = ''

    return render_template('index.html', form=form, name=session.get('name'), institution=session.get('institution'), subject=session.get('subject'), remote_ip=remote_ip, application_host=application_host, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404