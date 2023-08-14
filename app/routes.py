from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import Contato
from app.models import ContatoModels
import time #Biblioteca de tempo

@app.route('/') #é possível utilizar somente a barra para determinar o caminho principal
@app.route('/index')
def index():
    return render_template('index.html', title='Elga Alamour')

@app.route('/contato', methods = ['GET','POST']) #Chamada dos métodos a serem utilizados
def contato():
    dados_formulario = None
    formulario = Contato() #ver forms.py
    if formulario.validate_on_submit(): #Não esquecer de colocar a desgraça desse parêntese dps do método pra não perder 15min de intervalo
        flash('Seu formulário foi enviado')
        #flash(mensagem) Mostra/retorna uma mensagem rápida, pop-up
        #time.sleep(2) #Tempo em que a mensagem aparecerá na sua tela depois de sumir
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        conteudo = formulario.conteudo.data
        novo_contato = ContatoModels(nome = nome, email = email, telefone = telefone, conteudo = conteudo)
        db.session.add(novo_contato) #Abre uma sessão e add um novo contato na mesma
        db.session.commit() #Envia para o banco de dados
        #return redirect('/contato') #vai mandar novamente para a rota contato
    return render_template('contato.html', title='Contato', formulario = formulario, dados_formulario = dados_formulario)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre mim')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html', title='Meus Projetos')