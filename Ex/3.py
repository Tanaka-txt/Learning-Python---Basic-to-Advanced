"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name_user = input('Whats your name? ')
age_user = input('Whats is your age? ')
if name_user != '' and age_user != '': 
  space = ' ' # Pega tamanho do nome para invertes
  invert_name = print(name_user[::-1]) # Inverte Name
  if space in name_user:
    print('True - Space')
  else:
    print('False - No Space')
  name_len = len(name_user)
  print(name_len)
  first_letter = print(name_user[0])
  last_letter = print(name_user[-1]) # João -> -3-2-1-0 (-1) = -1 é o primeiro indice ao contrário

else:
  print('Desculpe, você deixou campos vazios.')