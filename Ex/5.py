"""
Iterando Strings com While
"""
       #012345678910
nome = 'Luiz Otávio' # Iteráveis, passar por indice e indice
novo_nome = ''

i=0
novo_nome = ''
while i < len(nome):
  letra = nome[i]
  novo_nome += f'*{letra}'
  i += 1

print(novo_nome)
