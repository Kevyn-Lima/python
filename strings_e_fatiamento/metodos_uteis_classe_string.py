#Classes em python upper(), lower(), title(), são algun métodos que podemos utilizar.

curso = "pYtHOn"

print(curso.upper())
print(curso.lower())
print(curso.title())

# Removendo espaços em branco, com os methodos, .strip(), .lstrip(), .rstrip()

curso = "   Python "

print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

#Junções e centralização .center(10, #) podemos utilizar com os caracters especificos e o numero de caracteres
# .join() adicionar em cada espaço.
curso = "Python"
print(curso.center(10,"#"))
print(".".join(curso))