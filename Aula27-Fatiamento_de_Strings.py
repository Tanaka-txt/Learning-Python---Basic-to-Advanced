"""
Fatiamento de string
 012345678
 Olá Mundo
-987654321

Fatiamento [inicio:fim:passo] [::]
Passo = Quantos em quantos caracteres ele vai pular
Obs.: a função len retorna a qtd de caracteres

"""
#      012345678 = 9 elementos
var = 'Olá Mundo'
indice = 'm'
print(len(var))
print(var[4:]) # Assim ele sabe que tem q começar no indice 4 e ir até o fim

print(var[2:7]) #á Mun (Não pega o indice 7, se eu quero que vá até o 7 eu pego o 8)
print(var[2:8]) # Com 8 (á Mund)

print(var[0:len(var):2]) # Começa no inicio e vai até o tamanho de 2 em 2 passo
# OáMno

print(var[::-1]) # Inverte String