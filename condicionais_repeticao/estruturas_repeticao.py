# # Exemplos com FOR

# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")
# print()

#Função built-in range.
#range(stop) -> range object
#range(start, stop[, step]) -> range object

print(list(range(4)))

#Utilizando range com for
for numero in range(0, 11):
    print(numero, end=" ")

print(" ")

#Exibindo a tabuada do 5

for numero in range(0, 51, 5):
    print(numero, end=" ")
