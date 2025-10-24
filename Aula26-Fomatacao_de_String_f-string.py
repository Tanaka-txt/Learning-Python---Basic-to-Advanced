"""
Esse é um pouco menos usado

Formatação básica de strings

s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade
> - esquerda)
< - Direita
^- Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flagas - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # Quero preencher a esquerda até preencher 10 caracteres
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:.1f}.') # Deixa com 1 casa decimal




