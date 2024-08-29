class Main:

    pass

print("Testando Projeto")

#Usado para trazer atributos da classe Cliente
from Cliente import Cliente
from Conta import Conta

#Criando um objeto novo e pasando os atributos dos metodos contrutores de outras classes
#Herença
c1 = Cliente("Luiz", "xxxxxx")
conta = Conta(c1.name, 132520, 0)

#Chamando isntancias, dadas para os valores de outras classes
print(c1)
print(c1.name, " e ", c1.n)
print(conta.titular, "Numero: ", conta.numero, "Seu saldo: ", conta.saldo)

#Chamando metodos criados da classe conta.
conta.deposita(100)
conta.saque(50)
conta.extrato()