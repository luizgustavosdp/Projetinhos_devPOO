class Conta:

    #Metodo Construtor
    def __init__(self,titular,numero,saldo): 
        self.saldo = 0 #Inicializei saldo com valor 0
        self.numero = numero #Atribuir numero ao atributo numero do objeto. 
        self.titular = titular

        def get_saldo(self): #Metodo para retornar o valor de saldo
            return self.saldo
        
        def set_Saldo(self, saldo): #Metodo definir ou atualizar saldo da conta
            if (saldo<0):
                print("Saldo não pode ser negativo") #Se o valor ficar menor que 0. Msg é mostrada
            else:
                self._saldo = saldo #Se não, o valor de saldo é atualizado
       
    #Criando o metodo para saque
    def saque(self, valor):
            if(self.saldo>=valor):
                self.saldo-=valor
                print("Saque realizado com sucesso")
            else:
                print("Saldo Insuficiente")

    #Criando metodos para deposito
    def deposita(self,valor):
            self.saldo+=valor

    #Criando metodo para extrato
    def extrato(self):
            print("Cliente: ",self.titular, "Saldo Atual: ", self.saldo)
