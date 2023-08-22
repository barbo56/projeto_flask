from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, session, redirect
from app.forms import Contato, Cadastro
from app.models import ContatoModels, CadastroModels
from flask_bcrypt import check_password_hash
import time #Biblioteca de tempo

@app.route('/') #é possível utilizar somente a barra para determinar o caminho principal
@app.route('/index')
def index():
    return render_template('index.html', title='Elga Alamour')

@app.route('/contato', methods = ['GET','POST']) #Chamada dos métodos a serem utilizados
def contato():
    #dados_formulario = None
    formulario = Contato() #ver forms.py
    if formulario.validate_on_submit(): #Não esquecer de colocar a desgraça desse parêntese dps do método pra não perder 15min de intervalo
        flash('Seu formulário foi enviado') #mensagem de envio do formulário
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
    return render_template('contato.html', title='Contato', formulario = formulario)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title = 'Sobre mim')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html', title = 'Meus Projetos')

@app.route('/cadastro', methods = ['GET','POST'])
def cadastro():
    cadastro = Cadastro()
    if cadastro.validate_on_submit():
        try:
            email = cadastro.email.data
            nome_usuario = cadastro.nome_usuario.data
            senha = cadastro.senha.data
            hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
            novo_cadastro = CadastroModels(email = email, nome_usuario = nome_usuario, senha = hash_senha)
            db.session.add(novo_cadastro)
            db.session.commit()
            flash('Seu cadastro foi realizado com sucesso')
        except Exception as erro: #Salva o erro na variável (recomendado o uso da variável "e" para armazenar o erro)
            flash('Ocorreu um erro ao cadastrar. Entre em contato com o suporte: zezindoserros@rapidmail.com')
            print(str(erro)) #Evitar concatenar o erro na mensagem flash, para que o usuário não veje o erro que ocasionou o problema
    
    return render_template('cadastro.html', title = 'Cadastre-se', cadastro = cadastro)

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == "POST":
        nome_usuario = request.form.get('nome_usuario')
        senha = request.form.get('senha')
        usuario = CadastroModels.query.filter_by(nome_usuario = nome_usuario).first() #Busca a primeira ocorrência, no banco de dados, da ocorrência digitada
        if usuario and check_password_hash(usuario.senha, senha): #Verifica se o usuário solicitado no banco de dados confere com o digitado na página
            session['nome_usuario'] = usuario.nome_usuario
            #session['email'] = usuario.email
            flash('Login efetuado com sucesso!')
            time.sleep(1) #Define o tempo que a pagina permanece em visualização antes de ser redirecionada
            return redirect(url_for('index'))
        else:
            flash('Nome de usuário ou senha incorreta')

    return render_template('login.html', title = 'Login')

@app.route('/sair')
def sair():
    session.pop('nome_usuario', None)
    #session.pop('email', None)
    return redirect(url_for('login'))

#A partir daqui foi onde faltei a aula, no caso de erro comentar todo o código até a marcação
@app.route('/editar', methods=['POST', 'GET'])
def editar():
    if 'nome_usuario' not in session:
        return redirect(url_for('login'))
    usuario = CadastroModels.query.filter_by(nome_usuario = session['nome_usuario']).first()
    #Porque não usar um elif aqui?
    if request.method == 'POST':
        usuario.nome_usuario = request.form.get('nome_usuario')
        usuario.email = request.form.get('email')
        senha = request.form.get('senha')
        usuario.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        db.session.commit()
        session['nome_usuario'] = usuario.nome_usuario
        session['email'] = usuario.email
        session['senha'] = usuario.senha
        
        flash('Dados atualizados com sucesso')
        return redirect(url_for('editar'))
    
    return render_template('editar.html', title = 'Editar dados', usuario = usuario)
#comentar até aqui