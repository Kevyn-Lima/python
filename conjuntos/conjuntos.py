#um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável

#Acessar os dados do set, conjuntos não suporta indexação e nem fatiamento, para isso, voce precisa converte-lo para uma lista

numeros = {1,2,3,4,2}
print(numeros)

numeros = list(numeros)
print(numeros[0])

#Forma mais comum para percorrer os dados de um conjunto é utilizando o comando for

carros = {"gol", "celta", "palio", "gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Acima podemos ver que podemos percorrer todo o set, porém como ele não duplica, não podemos validar tudo, mas ele mostra o indice também.


#Métodos da classe set .union()
conjunto_a = {1,2}
conjunto_b = {3,4}


print(conjunto_a.union(conjunto_b))

#Método .intersection(), tras o que é igual dos dois conjuntos.

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.intersection(conjunto_b))

#Assim como o .difference(), que traz o que é diferente em ambos os conjuntos.

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#.symmetric_difference() traz todos os elementos que não estão na interseção

print(conjunto_a.symmetric_difference(conjunto_b))

#.issubset() valida se todos os elementos de um conjunto estão em outro "is sub set"

conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#.issuperset() valida ao contrário, se todos os conjuntos de b, estão em a.
#.isdisjoint() valida se um valor tem em um conjunto com o outro conjunto.

#.add(), nele voce pode passar um elemento que é adicionado a ele, se passar um elemento ja existente, ele ignora o que foi passado.
# .clear(), .copy(), .discard() o discard, discarta o valor que foi passado, apenas o que existe dentro do set.
#.pop(), retira os valores do set sem passar parametros, retira em sequencia.
#remove(), segue como o discard, a diferença dos dois é que o remove gera erro se o elemento não existir.
#assim como o len(), se quiser validar se tem um objeto dentro do conjunto, podemos utilizar o valor in.

