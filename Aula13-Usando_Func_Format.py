a = 'A'
b = 'B'
c = 1.1
# tudo em python é um objeto e, todos os objetos tem métodos dentro deles, se eu por um...
# ponto na string ele vai me dizer oque eu tenho acesso a string

# Esses são os metodos = Ações que um obejto pode fazer

formatar1 = 'a={} b={} c={:.2f}'.format(a,b,c) # Método format
#                               indices:0,1,2

print(formatar1)

formatar2 = 'a={0} b={1} c={2:.2f}'.format(a,b,c) # Chamando por indices
print(formatar2)

#formatar = 'a={} b={} c={:.2f}'.format(Passo as variaveis aqui ex. a,b,c [argumentos / parametro])
#           São as strigs em ordem

#Parametro Nomeado - Quando dou nome para as coisas dentro do chamado das funções
formatar3 = 'a={nome1} b={nome2} c={nome3:.2f}'.format(
  nome1= a, #Nome1 - Parametro = Argumento 'a'
  nome2 = b, #Nome2 - Parametro = Argumento 'b'
  nome3 = c #Nome3 - Parametro = Argumento 'c'

  ) # Chamando por indices
print(formatar3)

#Quando a função está dentro de um objeto é chamado de method