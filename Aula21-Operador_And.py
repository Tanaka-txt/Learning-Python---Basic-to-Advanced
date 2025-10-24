# Operador lógico

#and (e)

entrada = input('[E]ntrar [S]air').lower()
#print(entrada)

senha_digitada = input('Senha: ')

senha_segura = '123456'

if entrada == 'e' and senha_digitada == senha_segura:
  print('Entrar')

elif entrada == 's': 
  print('Saida')

else:
  print('Invalid Option!')

# _____________________
#|  A  |  B  |   AND   |
#|  1  |  1  |    1    |
#|-----|-----|---------|
#|  1  |  0  |    0    |
#|-----|-----|---------|
#|  0  |  1  |    0    |
#|-----|-----|---------|
#|  0  |  0  |    0    |
#|_____|_____|_________|
