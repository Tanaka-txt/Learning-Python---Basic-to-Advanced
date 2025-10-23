# if /    elif   / else
# se / se não se / se não

entrada = input('Digite entrar ou sair, para prosseguir: ')

if entrada == 'entrar':
  print('Entrando no sistema.')
  print('Entrando no sistema..')
  print('Entrando no sistema...')
  idade = int(input('Qual sua idade? '))
  #print(type(entrada))

  if idade < 18:
    print('Você não pode dirigir')
  else:
    print('Você pode dirigir!')

elif entrada == 'sair':
  print('Saindo do código')

else:
  print('Valor digitado errado')

