"""
Calculadora com While
"""
opcao = 999

while True:
  numero_1 = input('Digite um Número: ')
  numero_2 = input('Digite outro Número: ')
  operador = input('Digite o Operador (+-/*): ')

  numeros_validos = None

  try:
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
    numeros_validos = True
  except:
    numeros_validos = None

  if numeros_validos is None:
    print('Um ou ambos os numeros digitador são inválidos')
    continue

  operadores_permitidos = '+-/*'

  if operador not in operadores_permitidos:
    print('Operador Inválido')
    continue

  if len(operador) > 1:
    print('Erro - Apenas 1 operador por vez!')
    continue

  if operador == '/' and numero_2 == 0:
    print('Operação Não pode ser feita Numero 2 é 0!')
    continue


  ##########################################

  if operador == '+':
    soma = numero_1 + numero_2
    print(f'Resultado da Subtração = {soma:.2f}')
  
  elif operador == '-':
    sub = numero_1 - numero_2
    print(f'Resultado da Subtração = {sub:.2f}')
  
  elif numero_2 != 0 and operador == '/':
    div = numero_1 / numero_2
    print(f'Resultado da Divisão = {div:.2f}')
  
  else:
    mult = numero_1 * numero_2
    print(f'Resultado da Multiplicação = {mult:.2f}')

  sair_ficar = input('Quer Sair? [s]im ou [n]ão ').lower().startswith('s' or 'n') # Se começar com s == True
  
  if sair_ficar is True:
      break
  else:
      continue 
  