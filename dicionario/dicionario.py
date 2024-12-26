#Um dicionario em Python, parece muito um objeto em JS, a diferença pelo o que entendi é que precisa receber 
#Chave: Valor, porém a chave, precisa ser algo imutável, segue abaixo, alguns exemplos.

pessoa = {
    "nome": "Kevyn", 
    "Idade": 25
}

print(pessoa)

pessoa = dict(
    nome = "Elizabeth",
    idade = 25
)
print(pessoa)

pessoa["telefone"] = "3333-1234"

print(pessoa)

#Para acessar cada chave, se torna algo bem simples, parecido muito com destructuring.

print(pessoa["nome"])

#Existe também o conceito de matriz em dicionario

contatos = {
    "teste01@gmail.com": {"nome": "Teste01", "telefone": "3333-2221"},
    "teste02@gmail.com": {"nome": "Teste02", "telefone": "3333-2222"},
    "teste03@gmail.com": {"nome": "Teste03", "telefone": "3333-2223"},
    "teste04@gmail.com": {"nome": "Teste04", "telefone": "3333-2224", "endereco": {"rua": "Joao Teodoro", "numero": 25}},
}

#Acessando eles de forma igual a lista
print(contatos["teste03@gmail.com"]["nome"])
print(contatos["teste04@gmail.com"]["endereco"]["numero"])

#Podemos iterar tambem com o for

# for chave in contatos:
#     print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)