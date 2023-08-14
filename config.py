import os #Biblioteca que tem acesso ao sistema operacional
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '@genteP256' #Caso ele não encontre senha ele irá optar por usar a senhar fornecida após o 'ou'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') #Contra barra busca na raiz do projeto                                                     
    SQLALCHEMY_TRACK_MODIFICATIONS = False