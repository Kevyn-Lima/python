# #Relembrando Estruturas condicionais dentro do Python.

# import sys


# saldo = 2000.0
# saque = float(input("Informe o valor do saque:"))

# if(saldo >= saque):
#     print("Realizando Saque")
# else:
#     print("Saldo Insuficiente")

# #Se precisar utilizar mais uma parte dentro do if é elif. != elseif

# opcao = int(input("Informe uma opção: [1] Sacar / n[2] Extrato: "))

# if(opcao == 1):
#     valor = float(input("Informe a quantia para saque: "))
# elif(opcao == 2):
#     print("Exibindo Extrato")
# else:
#     sys.exit("Opção inválida.")

# #IF Aninhado
# conta_normal = True 
# conta_universitaria = True
# cheque_especial = 450

# if conta_normal:
#     if saldo >= saque:
#         print("Saque realizado com sucesso.")
#     elif saque <= (saldo + cheque_especial):
#         print("Saque realizado com o uso de cheque especial")
#     else:
#         print("Não foi possível realizar o saque, saldo insuficiente.")
# elif conta_universitaria:
#     if saldo >= saque:
#         print("Saque realizado com sucesso.")
#     else:
#         print("Saldo insifuciente")

#if Ternário

saldo = 2100
saque = 2730

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")