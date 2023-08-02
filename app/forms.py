from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField
from wtforms.validators import DataRequired

class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    telefone = TelField('telefone', validators=[DataRequired()])
    conteudo = TextAreaField('conteudo', validators=[DataRequired()])