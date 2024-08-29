class main:

 from funcionario import funcionario


 luiz = funcionario("luiz", 1236, "luiz@seila.com")

#Adicionando o agurmento para cada função
 luiz.cadastro_horas("Janeiro", 120)
 luiz.cadastro_horas("Fevereiro", 24)

 luiz.cadastro_salario("Janeiro", 80)
 luiz.cadastro_salario("Fevereiro",100)

 luiz.cadastro_horas("Março", 80) #A função que irá registrar horas trabalhadas 
 luiz.cadastro_salario('Março', 50)# A função que irá registrar salario por hora trabalhada referente ao mes

 #Atraves da função __repr__ o objeto é capaz se de "auto_apresentar"
 print(luiz)

 #Chamando os metodos responsaveis por fazer o calculo referente ao mes argumentado
 print(luiz.calcular("Janeiro"))
 print("Este mês você tem R$", luiz.calcular("Fevereiro"))
 print(f"Este mês tem R${luiz.calcular("Março"):.2f}")