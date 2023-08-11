from app import app, db

class Contato_Models(db.Model):
    id = db.Column(id.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    telefone = db.Column(db.String(14), nullable = False)
    conteudo = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return f'<Contato {self.nome}>'