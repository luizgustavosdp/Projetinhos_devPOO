class bibliotecaFilmes:

 #O Código irá registrar nome, tempo (em minutos) e nota do filme
 def __init__(self, filme):
     self.filme = filme # Nome do Filme
     self.duracao = {} #Duração do Filme em minutos
     self.nota = {} #Nota do filme

 #Resgistro Duracao do filme
 def registrarDuracao(self, minutos):
       self.duracao = minutos

 #Resgistro Nota do filme e nome do usuario que deu aquela nota
 def registrarNota(self, nome, avaliacao): 
     if(avaliacao not in self.nota):
       self.nota[nome] = avaliacao

 def __repr__(self):
  return f'\nFilme: {self.filme}\nDuração: {self.duracao}min\nNota: {self.nota}'

