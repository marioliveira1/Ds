class Pessoa:
    nome = ""
    cpf = ""
    data_nasc = ""
    telefone = ""
    email =""

    # CONSTRUTOR
    def __init__(self, nome, cpf, email):
      self.come = nome 
      self.cpf = cpf
      self.email = email

    def apresentarSe(self):
        print("Olá, sou uma pessoa! Meu nome é {self.nome}")
    