#Métodos da classe list.

#.append() ou seja, lista.append("1")
#.clear() utilizado para limpar a lista inteira.
#.copy() retorna um alista igual, porém com instancia diferente, sendo assim, outra lista.

lista = [1,"Python", [40, 30, 20]]
l2 = lista.copy()
l2.append("Adicionei aqui")

print(lista)
print(l2)

print(id(l2), id(lista))

#.count() Utilizando para contar quantas vezes, um determinado objeto aparece dentro da lista
#.extend(), muito utilizado, para adicionar novos elementos nela, assim como uma outra lista dentro de uma unica.
linguagens = ["python", "js", "C"]
print(linguagens)
linguagens.extend(["Java", "csharp"])
print(linguagens)

#.index() no index, podemos validar a primeira vez que aparece o objeto.
print(linguagens.index("Java"))
print(linguagens.index("python"))

#.pop() utilizando para retirar o ultimo elemento da lista, porém, como parametro, pode passar o indice de qual voce quer retirar da lista
#.remove(), uma outra forma para retirar algo da lista, diferença que se passa o objeto em si.
#.reverse(), realiza o espelhamento dela, como um espelho mesmo.
#.sort(), ele ordena a lista, sendo primeiro de maneira alfabetica.
#Agora com argumentos, como .sort(reverse=True), ou .sort(key=lambda x: len(x))
#.len(), o tamanho da lista
#sorted(), servindo para ordenar interáveis, sendo como uma função, ele tem que ser passado primeiro, como o sort.

