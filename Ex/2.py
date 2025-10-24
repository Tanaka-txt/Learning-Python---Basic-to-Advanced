primeiro_valor = int(input('Digite o valor: ')) # Volta string
segundo_valor = int(input('Digite outro valor: ')) # Volta string

#Ele vai retornar qual valor é maior usando tabela unicode, então não precisaria convertes, mas é melhor

# If o valor é maior ele é exibido primeiro, se o valor é menor ele é exibido depois

if primeiro_valor == segundo_valor:
  print('Numeros iguais')

elif primeiro_valor > segundo_valor:
  print(
    f'{primeiro_valor}, {segundo_valor}'
    ) 
else :
  print(
    f'{segundo_valor}, {primeiro_valor}'
    )