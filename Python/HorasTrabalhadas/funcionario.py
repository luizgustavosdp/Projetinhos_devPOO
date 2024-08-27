class funcionario:

 def __init__(self,nome, matricula, email):
   self.nome = nome
   self.matricula = matricula
   self.email = email
   self.horas = {} #Irá armazena horas trabalhadas no mes
   self.salariohora = {} #Irá armazena salario por horas trabalhadas no mes

 #Verifica se mes está resgitrado. Se não tiver, adiciona o mes no dicionario junto com as horas.
 #Faz o registro utilizando as matriz para vincular o mes com o valor
 def cadastro_horas(self, mes, horas):
    if( mes not in self.horas):
     self.horas[mes] = horas

 #Verifica se mes está resgitrado. Se não tiver, adiciona o mes no dicionario junto com salario (por hora trabalhada)
 def cadastro_salario(self,mes, salario):
   if(mes not in self.salariohora):
     self.salariohora[mes] = salario
    
 #Calcula o valor de horas trabalhadas no mes, vezes o salario trabalhado no mes
 def calcular(self, mes):
   if(mes not in self.horas) or (mes not in self.salariohora):
      print("Mês não cadastrado")
   else:
      return self.horas[mes] * self.salariohora[mes]
   
 def __repr__(self):
  return f'\nFuncionario: {self.nome}, \nEmail: {self.email},\nHoras/mes: {self.horas},\nSalariohora {self.salariohora}\n'