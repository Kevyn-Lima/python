frutas = ["Laranja", "Maçã", "Uva"]
frutas = []
letras = list("python")

print(letras)
numeros = list(range(1,11))
print(numeros)

#Funciona normalmente como qualquer outro array, porém voce pode acessar com -1 onde pega o ultimo, e se for diminuindo mais
#Como -2, -3, ele segue pegando do ultimo para o primeiro.
#Agora um exemplo de fatiamento.

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

#Utilizando for

carros =  ["Gol", "Celta", "Palio", "Civic"]

for carro in carros:
    print(carro)

#Função enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Filtros, bem parecido com o map em JS.

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

#Outra forma de ser realizado tal ação, seria pelo comprehension

impares = [numero for numero in numeros if numero % 2 != 0]

print(impares)