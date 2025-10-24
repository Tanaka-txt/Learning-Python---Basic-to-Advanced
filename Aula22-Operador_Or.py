# Operador lógico

#or (ou)

# Falsy
# 0 0.0 '' False

entrada = input('[E]ntrar [S]air :')
#print(entrada)

senha_digitada = input('Senha: ') or 'Sem Senha' # If em uma linha só com or


senha_segura = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_segura:
  print('Entrar')

elif (entrada == 'S' or entrada == 's'): 
  print('Saida')

else:
  print(senha_digitada)


# Avaliação de Curto Circuito
print(True or False) # True
print(0 or False or 0 or 'abc') # True por conta do Trufy


# _____________________
#|  A  |  B  |   OR    |
#|  1  |  1  |    1    |
#|-----|-----|---------|
#|  1  |  0  |    1    |
#|-----|-----|---------|
#|  0  |  1  |    1    |
#|-----|-----|---------|
#|  0  |  0  |    0    |
#|_____|_____|_________|
