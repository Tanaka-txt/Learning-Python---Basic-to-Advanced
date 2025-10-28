"""
CONSTANTE =  "Variaveis" que não vão mudar
Muitas condições no mesmo IF (Ruim)
          <- Contagem de Complexidade (Ruim) - Tab muitos grandes é ruim
"""

# No python não temos a a variavel CONST (Constante) = Var que nunca muda
#Temos uma Convenção sobre coisas que nunca vão mudar no código

# Variaveis constantes!!!!!
# * Ficam em Maísculo

RADAR_1 = 60 # Velocidade do radar
LOCAL_1 = 100 # Local onde o radar está
RADAR_RANGE = 1  # Vai estar em 99 e 101

#-=======================================-

# Ruim por muitas condições dentro de um IF

#-=======================================-

# Essas var server como var de mudança
velocidade = 61 # Velocidade atual
local_carro = 90 # Local que o carro está na estrada

#-=======================================-

velocidade_do_carro_esta_a_cima_permitido = velocidade > RADAR_1

carro_esta_no_range = (local_carro >= LOCAL_1 - RADAR_RANGE) and (local_carro <= LOCAL_1 + RADAR_RANGE)

if velocidade_do_carro_esta_a_cima_permitido:
  print('Passou da velocidade do Radar')
  if carro_esta_no_range:
    print('Carro Foi MUltado')
  else: # Não Está no Range
    print('Carro não foi multado')
else : # Não está a com velocidade a cima
  print('Não Estava a cima da velocidade')
