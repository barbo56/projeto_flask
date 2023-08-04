from app import app
from flask import render_template, url_for, flash, redirect, request
from app.forms import Contato
import time #Biblioteca de tempo

@app.route('/') #é possível utilizar somente a barra para determinar o caminho principal
@app.route('/index')
def index():
    return render_template('index.html', title='Elga Alamour')

@app.route('/contato', methods = ['GET','POST']) #Chamada dos métodos a serem utilizados
def contato():
    dados_formulario = None
    formulario = Contato() #ver forms.py
    if request.method == 'POST':
        flash('Seu formulário foi enviado')
        #flash(mensagem) Mostra/retorna uma mensagem rápida, pop-up
        #time.sleep(2) #Tempo em que a mensagem aparecerá na sua tela depois de sumir
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        conteudo = request.form.get('conteudo')

        dados_formulario = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'conteudo': conteudo
        }
        #return redirect('/contato') #vai mandar novamente para a rota contato
    return render_template('contato.html', title='Contato', formulario = formulario, dados_formulario = dados_formulario)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre mim')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html', title='Meus Projetos')