#--------------------------------------------------------------------------
# Concatenação(+) e Repetição (*)
concatena = 'A' + 'B' + 'C'
print(concatena)

repete_10_vezes = 'A' * 10
repete_3_vezes = 3 * 'Luiz'
print(repete_10_vezes)
print(repete_3_vezes)

cuidado1 = 'Luiz' + ' ' + 'Otávio'
#cuidado2 = 'Luiz' + 1 +' ' + 'Otávio' - Da Erro python não sabe oque fazer pois juntamos string e number
cuidado2 = 'Luiz' + str(1) +' ' + 'Otávio' # Forma certa
print(cuidado1)
print(cuidado2)
#--------------------------------------------------------------------------