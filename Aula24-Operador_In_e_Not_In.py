#  Operadores in e not in
#  Strings são iteráveis
#  0 1 2 3 4 5  --- Indices
#  O t á v i o  --- Indices
# -6-5-4-3-2-1  --- Indices

# in = entre (Está entre)
# not in = não entre (Não está entre)

# Iterável = Possibilidade de navegação de elemento em elemento

#       012345
nome = 'Otávio'
print(nome[2]) # Quero acessar o indice do 'á'

print('á' in nome) # Quero checar se á esta entre as letras do nome, se estiver = True
print('vio' in nome) # True

print('z' not in nome) # Vejo se 'z' não está entre as letras do nome, se não estiver = True
print('vio' not in nome) # False, pois ele está

nome_user = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')


if encontrar in nome: # Se oque ele deseja encontrar está contido em nome
  print(f'{encontrar} está contino no {nome}')

else :
  print(f'{encontrar} não está em {nome}')