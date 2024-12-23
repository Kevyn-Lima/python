#Reforçando operadores de identidade.

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

validacao = curso is nome_curso
print(validacao)

validacao = curso is not nome_curso
print(validacao)

validacao = saldo is limite
print(validacao)