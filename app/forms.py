from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

#csrf = CSRFProtect(app)

class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    telefone = TelField('telefone', validators=[DataRequired()])
    conteudo = TextAreaField('conteudo')
    enviar = SubmitField('Enviar')

class Cadastro(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    nome_usuario = StringField('nome_usuario', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    nome = StringField('nome', validators=[DataRequired()])
    sobrenome = StringField('sobrenome', validators=[DataRequired()])
    endereco = StringField('endereco', validators=[DataRequired()])
    numero_endereco = StringField('numero_endereco', validators=[DataRequired()])
    bairro = StringField('bairro', validators=[DataRequired()])
    cidade = StringField('cidade', validators=[DataRequired()])
    uf = StringField('uf', validators=[DataRequired()])
    cpf = StringField('cpf', validators=[DataRequired()])
    enviar = SubmitField('Enviar')