# Operador lógico

#Not (não)
# True == False
# False == True

# Falsy
# 0 0.0 '' False

entrada = input('[E]ntrar [S]air :').lower()
#print(entrada)

senha_digitada = input('Senha: ') or 'Sem Senha' # If em uma linha só com or


senha_segura = '123456'

if (entrada != 'r' or entrada != 's'):
  print('Entrada invalida')

elif entrada == 'S' or entrada == 's' :
  print('Saida')

else:
  if senha_digitada != senha_segura:
    print('Senha inválida!')
  else:
      if (entrada == 'E' or entrada == 'e'):
        print('Entrar')




# _____________________
#|  A  |  B  |   NOT   |
#|  1  |  1  |    0    |
#|-----|-----|---------|
#|  1  |  0  |    0    |
#|-----|-----|---------|
#|  0  |  1  |    0    |
#|-----|-----|---------|
#|  0  |  0  |    2    |
#|_____|_____|_________|
