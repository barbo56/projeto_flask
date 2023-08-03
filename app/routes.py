from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import Contato
import time #Biblioteca de tempo

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Elga Alamour')

@app.route('/contato', methods = ['GET', 'POST']) #Chamada dos métodos a serem utilizados
def contato():
    formulario = Contato()
    if formulario.validate_on_submit(): #Validação para saber se o botão 'enviar' do formulário foi pressionado
        mensagem = flash('Seu formulário foi enviado')
        flash(mensagem) #Mostra/retorna uma mensagem rápida, pop-up
        time.sleep(2) #Tempo em que a mensagem aparecerá na sua tela depois de sumir
        return redirect('contato')

    return render_template('contato.html', title='Contato', formulario = formulario)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre mim')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html', title='Meus Projetos')