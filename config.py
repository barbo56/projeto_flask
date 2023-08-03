import os #Biblioteca que tem acesso ao sistema operacional

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'agentep256' #Caso ele não encontre senha ele irá optar por usar a senhar fornecida após o 'ou'