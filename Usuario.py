class Usuario(object):

    def __init__(self):
        self.nome = str
        self.login = str
        self.senha = str
        self.email = str

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setLogin(self, login):
        self.login = login

    def getLogin(self):
        return self.login

    def setSenha(self, senha):
        self.senha = senha

    def getSenha(self):
        return self.senha

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def __repr__(self):
        return f' Nome: {self.getNome()}\n Email: {self.getEmail()}'