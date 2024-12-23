# Reforçãndo operadores lógicos em Python

saldo = 1000
saque = 200
limite = 100
consta_especial = True
validacao = saldo >= saque and saque <=limite

print(validacao)

validacao = saldo >= saque or saque <=limite

print(validacao)

validacao = (saldo >= saque and saque <= limite) or (consta_especial and saldo >= saque)

print(validacao)