
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_int_user = input('Digite um número inteiro: ')
numero_pair_or_odd = None

try:
  conver = int(numero_int_user) # Verificamos se é possivel fazer conversão, se der erro ele vai pro outro
except:
  print('Não é um numero inteiro')

if conver % 2 == 0:
  print('Par')

else : 
  print('Impar')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hour_user = input('Digite que Horas São xx :')

try:
  conver1 = int(hour_user)
except:
  print('Digite um Número inteiro')

if conver1 >= 0 and conver1 <= 11:
  print('Bom Dia!')

elif conver1 >= 12 and conver1 <= 17:
  print('Boa Tarde!')

else:
  print('Boa Noite!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
name_user = input('Digite Seu nome: ')

size_name = len(name_user) # Se < 4 nome curto

if size_name <= 4:
  print(f'{name_user}. Seu nome é curto')

elif size_name >= 5 and size_name <= 6:
  print(f'{name_user}. Seu nome é normal')

else:
  print(f'{name_user}. Seu nome é muito grande')