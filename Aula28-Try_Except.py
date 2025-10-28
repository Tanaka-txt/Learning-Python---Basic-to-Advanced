"""
Introdução ao Try/ Except
try -> Tentar executar
Except -> Ocorreu algum erro ao tentar executar
"""

# Exemplo
print(234)
print('abc')

#int('a') # Estou tentando converter uma string em numero Erro
#Traceback (most recent call last):
#  File "/home/julio/Desktop/Geral/Estudos/Python/Aula28-Try_Except.py", line 11, in <module>
#    int('a') # Estou tentando converter uma string em numero Erro
#    ~~~^^^^^
#ValueError: invalid literal for int() with base 10: 'a'


numero_str = input (
  'Vou dobrar o numero que você digitar: '
)

#numero_str.isdigit # Checa se o user digitou apenas numeros vai retornar boole false ou true

try: # Tenta executar este código (FAIL FAST), ele ve algo errado já vai pro Except
  print(f'STR: {numero_str}')
  numero_float = float(numero_str)
  print(f'FLOAT: {numero_float}')
  print(f'O dobro de {numero_str} é {numero_float * 2}')
except: # Se ocorrer algum erro dentro do try, pula pro except
  print('Isso não é um numero')