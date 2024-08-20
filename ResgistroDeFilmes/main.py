class Main:

 from bibliotecaFilmes import bibliotecaFilmes

 godfather = bibliotecaFilmes("Godfather")

 godfather.registrarDuracao(120)

 godfather.registrarNota("Luiz",9.5)
 godfather.registrarNota("Pedro",9)
 godfather.registrarNota("Yoshi",4)
 godfather.registrarNota("Luigi",7)

 print("\nO Filme: ", godfather.filme, "\nDuração:", godfather.duracao,"min","\nNota",godfather.nota,"\n")