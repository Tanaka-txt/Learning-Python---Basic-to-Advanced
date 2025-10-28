"""
Sobre documentação 
https://docs.python.org/pt-br/3/library/stdtypes.html

Tipos embutidos em Python

Imultávei que vimos = str, int, float, bool (Não podemos altera-los)
"""

# Exemplo:

string = 'Luiz Otávio'

# string[3] = 'ABC' Não pode ser alterado desta forma

# Para alterar crie outra string

outra_str = f'{string[:3]}ABC{string[4:]}'

print(string)
print(outra_str)

# Essas imultaveis são variaveis que tem metódos pois são Objetos