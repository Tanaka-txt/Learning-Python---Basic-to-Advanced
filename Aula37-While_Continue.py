"""
Repetições
While (enquanto)

Executa uma ação enquanto uma condição for verdadeira
"""

contador = 0 

while contador < 100:
  #contador = contador + 1
  contador += 1

  if contador == 6: # Vai pular o 6
    print('Não Vou Mostrar o 6')
    continue

  print(contador)

  if contador == 40:
    break
    
print('\n')
