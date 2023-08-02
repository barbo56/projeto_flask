from app import app
from flask import render_template
from app.forms import Contato

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Elga Alamour')

@app.route('/contato')
def contato():
    return render_template('contato.html', title='Contato')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre mim')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html', title='Meus Projetos')

@app.route('/enviar_contato')
def enviar_contato():
    formulario = Contato()
    return render_template('contato.html', title='Meus Projetos')