from app import app, db

class ContatoModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False) #nullable garante que o campo não pode ser vazio
    email = db.Column(db.String(50), nullable = False)
    telefone = db.Column(db.String(14), nullable = False)
    conteudo = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return f'<Contato {self.nome}>'
    
class CadastroModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    nome_usuario = db.Column(db.String(10), nullable = False, unique = True)
    senha = db.Column(db.String(10), nullable = False)
    nome = db.Column(db.String(10), nullable = False)
    sobrenome = db.Column(db.String(10), nullable = False)
    endereco = db.Column(db.String(20), nullable = False)
    numero_endereco = db.Column(db.String(10), nullable = False)
    bairro = db.Column(db.String(10), nullable = False)
    cidade = db.Column(db.String(10), nullable = False)
    uf = db.Column(db.String(20), nullable = False)
    cpf = db.Column(db.String(20), nullable = True)

    '''def __repr__(self):
        return f'<Contato>'''