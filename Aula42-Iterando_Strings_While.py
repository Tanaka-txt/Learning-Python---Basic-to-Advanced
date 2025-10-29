frase = 'O pytoh é uma linguagem de programção' \
  'multiparadigma.' \
  'Python foi criado por Guido van Rossum.'

# .count('Python') = Fala quantas vezes a palavra python apareceu

#print(frase.count('a'))
#print(frase.count('b'))
#print(frase.count('c'))
#print(frase.count('d'))
#print(frase.count('e'))
#print(frase.count('f'))
#print(frase.count('g'))
#print(frase.count('h'))
#print(frase.count('i'))
#print(frase.count('j'))
#print(frase.count('k'))
#print(frase.count('l'))
#print(frase.count('m'))
#print(frase.count('n'))
#print(frase.count('o'))
#print(frase.count('p'))
#print(frase.count('q'))
#print(frase.count('r'))
#print(frase.count('s'))
#print(frase.count('t'))
#print(frase.count('u'))
#print(frase.count('v'))
#print(frase.count('w'))
#print(frase.count('x'))
#print(frase.count('y'))
#print(frase.count('z'))

i = 0 
maior = 0
registrador = ''

while i < len(frase):
  letra_atual = frase[i] # Vai passar frase[0] = O, frase[1] = , frase[2] = p
  
  if(frase[i] == ' '):
    i += 1
    continue

  contagem_atual = frase.count(letra_atual)

  if contagem_atual > maior:
    maior = contagem_atual
    registrador = i
  
  i += 1

print(f'A letra com maior aparição foi\n Letra: "{frase[registrador]}" com Total: {maior}')