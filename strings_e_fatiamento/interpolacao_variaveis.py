# Existem 3 formas de interporlar strings em python, %, format e f, sendo mais utilizadas as duas ultimas.
#Método format, dentro elas, a melhor seria mesmo a f, como ja utilizamos anteriormente.
nome = "Kevyn"
idade = 25
profissao = "Data Engineer"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome,idade,profissao,linguagem))

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao}, estou matriculado no curso de {linguagem}")


#Imagine que tenha um float muito grande, porém voce deseja apenas apresentar duas casas
#decimais desse numero, podemos utilizar da seguinte maneira, assim passamos o numero de casas que querermos.
#Formatar strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
