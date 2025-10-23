# input().isascii = Recebe apenas ascii

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

your_year = input('Qual ano você nasceu? ')

ano_atual = 2025

idade = ano_atual - int(your_year)

print(f'Sua idade é {idade}')

# Input sempre retorna string, ou seja, precisamos as vezes converte-lo