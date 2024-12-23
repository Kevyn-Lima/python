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

# import sys


# print(list(range(4)))

# #Utilizando range com for
# for numero in range(0, 11):
#     print(numero, end=" ")

# print(" ")

# #Exibindo a tabuada do 5

# for numero in range(0, 51, 5):
#     print(numero, end=" ")

# print(" ")
# #Comando While em python

# opcao = -1
# while opcao !=0:
#     opcao = int(input("[1] Sacar\n[2] Extrato \n[0] Sair \n: "))

#     if opcao == 1:
#         print("Sacando...")
#     elif opcao == 2:
#         print("Exibindo...")
# else:
#     print("Obrigado por usar nosso sistema bancário, até logo.")


opcao = -1
while opcao != 0:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break
    print(opcao)
#Apenas validando um break como em switch case em JS, como o continue, que pula algo dentro do laço