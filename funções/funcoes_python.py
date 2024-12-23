def exibir_mensagem():
    print("Ola, mundo.")

exibir_mensagem()

#def é uma palavra reservada para declaração da função.

def mensagem_nome(nome):
    print(f"Ola, eu me chamo {nome}")

mensagem_nome("Carlos")

 # Exemplos de retornos em python.

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10,20,30]))
print(retorna_antecessor_e_sucessor(15))

#Um exemplo de retorno com kwargs.

def salvar_carro(modelo, ano, placa, marca):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
#aqui, vamos passar os parametros por chave: valor, como um objeto.
salvar_carro(**{"marca": "Fiat", "modelo":"Palio", "ano": 199, "placa":"ABC-1234"})
#Pois assim, mesmo que a ordem dos parametros sejam diferentes, ele vai funcionar da mesma forma.
print(" ")
# Outro exemplo com *args e **kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)

    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])

    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Segunda-Feira, 23 de Dezembro 2024","Zen of Python", "Beautiful is better than ugly.", autor = "Tim Peters", ano = 1999)

#Mais um exemplo de uma função

def somar(a,b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operacao {a} + {b} = {resultado}")

exibir_resultado(10, 25, somar)


#Varivaveis de escopo global

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario
salario_com_bonus = salario_bonus(500)

print(salario_com_bonus)