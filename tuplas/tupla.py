#São estruturas de dados muito parecidas com as listas, a principal diferenã é que tuplas são imutáveis, enquanto listas
#são mutaveis. Podemos criar tuplas através da classe "tuple", ou colocando valores separados por vírgula dentro de parenteses.

#Exemplo:

frutas = ("Laranja", "pera", "uva",) #Uma boa pratica colocar uma virgula ao final quando declarar uma tupla, para que não ocorra bug
letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

#Para acessar os valores de uma tupla.

frutas = ("maca", "laranja", "uva", "pera",)
print(frutas[0])
print(frutas[2])

#Existe uma matriz de tupla, sendo tuplas aninhadas.

#fatiamento, exatamente igual a array