#.clear() contatos.clear() exclui todos os valores do dicionario.
#.copy() identico aos demais ja validado, ele tira uma cópia do nosso dicionario.

contatos = {
    "nome": "Teste01", 
    "telefone": "3333-2221",
}

copia = contatos.copy()
copia["teste01@gmail.com"] = {"nome":"Jo"}

print(copia)

#.fromkeys() metodo cria chaves para você em duas situações, primeira quando quer criar em seu dicionario e somente
#colocar ela la, sem passar valor, apenas informar quais chaves voce deseja que ele cria, e o valor seria none.
dict.fromkeys(["nome", "telefone"])

# a segunda situação é quando voce quer colletar um conjunto de chaves, e colocar um valor padrão nelas.
dict.fromkeys(["nome", "telefone"], "vazio") 

#.get() uma segunda forma de acessar valores no dicionario, um método utilizado bastante.
print(contatos.get("teste01@gmail.com",{}))

# .items() Retorna uma lista de tuplas, muito util para se passar pelas tuplas com o for, como mencionado no exemplo de dicionario.py
print(contatos.items())

#keys() retorna somente a chave, em array
print(contatos.keys())

#.pop(), remove uma chave do seu dicionario, pode colocar a chave, se encontrar ele retorna o valor de remoção, se não voce
#pode colocar para retornar um valor apenas informando.

print(contatos.pop("kevyn@gmail.com", "Não foi possível encontrar essa chave."))

#.popitem(), a diferença é que não informa a chave e ele retira na seguencia

#.setdefault(), se o atributo não existir no dicionario, ele insere o valor que foi determinado.
# se existir, ele retorna o valor que existe no dicionario e não altera ele.

print(contatos.setdefault("nome", "Kevyn")) 

#.update(), permite que possamos atualizar o nosso dicionario, com um novo dicionario

#.values(), retorna somente os valores, como o método keys.

#método in, com uma forma de validar se uma chave existe ou não dentro do nosso dicionario.

lista_chaves: list = contatos.keys()

resultado = "kevyn@gmail.com" in contatos
print(resultado)

#del uma outra forma de retirar um valor, voce passa o objeto que deseja remover.

del contatos["telefone"]
print(contatos)