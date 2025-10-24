"""
Interpolação básica de string
s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF0123456789)

Mesma ideia fo format print(f'...{var}')
"""

nome = 'Luiz' # String
preco = 1000.95897643 #float
#variavel = 'Luiz, o preço total foi R$1000.95'
var = '%s, preço total foi de R$%.2f' % (nome, preco)
# %s = string
# %f = float
# %x = hexadecimal
# %d Numero int

print(var)

print('O hexadecimal de %d é %08x' % (1500, 1500))