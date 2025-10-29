"""
Repetições
While (Enquanto)
Exceuta enquanto uma condição não for verdadeira

Loop Infinito -> Quando o Código não tem fim
"""

condicao = False

while condicao:
  nome = input('Qual Seu Nome? ')
  print(f'Seu nome é {nome}')

  if nome == 'Sair':
    break # Sai do while

contador = 0 

while contador < 10:
    print(contador)
    contador = contador + 1
  