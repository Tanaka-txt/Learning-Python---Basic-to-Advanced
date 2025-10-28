"""
Flag (Brandeira) - Marcar um local

None = Não Valor

is e is nor = é ou não é (Tipo, valor, identidade)

id = Identidade
- Como o python busca a variaveil na memória
"""

v1 = 'a' # Var é dar um apelido para um valor que está na memória
v2 = 'a'
v3 = 'b'

print(id(v1)) # Tipo endereço?
print(id(v3))
print(id(v2)) # Por conta do python tentar ser eficiente
# Ele vai ver que os 2 valores dessas variaveis é a mesmo então vão entregar o mesmo id


# Quero saber se o interpretador passou por um local (Algoritmo)

condicao = False
passou_no_if = None # Forma de definir uma var, pois é ruim usarmos uma var que só está definida dentro do if

if condicao:
  passou_no_if = True
  print('Faça Algo')
else:
  #passou_no_if = False
  #Fica None sem o False
  print('Não Faça Algo')

#print('Passou no IF',passou_no_if)

print(passou_no_if, passou_no_if is None) # Se for None, não passou no IF
print(passou_no_if, passou_no_if is not None) # Se passou muda pra True, is not none