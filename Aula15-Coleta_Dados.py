# input().isascii = Recebe apenas ascii

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

your_year = input('Qual ano você nasceu? ')

ano_atual = 2025

idade = ano_atual - int(your_year)

print(f'Sua idade é {idade}')

# Input sempre retorna string, ou seja, precisamos as vezes converte-lo

input().strip # remove os espaços em branco

# Normaliza o texto indepedente de como o usuário escrever
input().upper #Converte todo o texto para maiúsculas.
input().lower #Converte todo o texto para minúsculas.

input().split # Se eu quero que o usuário digite varios valores separados de uma vez

input().capitalize # Só a primeira letra maiúscula

input().title #Toda palavra começa com maíuscula

input().lower # tudo minusculo

input().upper # tudo maiusculo

input().swapcase # Inverte a caixa de cada letra

input().casefold # Versão mais agressiva do lower(), comparação internacional

# Verificação no Input

input().islower # Tudo é minusculo
input().isupper # Se tudo é maiusculo
input().tittle # Se está na forma de Tittle String 'Tittle Case'
input().isalpha # Se é letra alfabetica
input().isdigit # Se é digito de 0-9
input().isdecimal # Similar ao isdigit(), porém mais restrito
input().isnumeric # MAis ampla aceita digitos, draçoes, ², etc..
input().isalnum # Se contem letra ou numero alpha numerico
input().isspace # Se contem espaço \t ou quebra linha \n
input().isprintable # Se todos os caracteres são inprimiveis ignora (\n)
input().isidentifier # Se string for um nome válido para uma variavel em python
input().isascii # Se todos os caracteres pertencem a tabela ascii

#Removação de caracteres
input().strip # remove espaço do inicio ao fim
input().lstrip # Remove espaço no Inicio (left-strip)
input().rstrip # Remove espaço no fim (right-strip)
input().removeprefix("pre") # Remove o prefixo 'pre'
input().removesuffix("suf") # Remove o sufico 'suf'

# Divisão e particionamento
input().split # Querba string nos espaços e retorna uma lista "Olá mmundp".split() --> ['Olá', 'mundo'] 
input().rsplit # Faz o mesmo que o split(), mas começa a quebrar pela direita
input().splitlines # Quebra a string nas quebras de linha '\n'
input().partition("sep") # Divide a string em 3 partes (oque vem antes do sep, o sep, oque vem depois do sep)
input().rpartition("sep") # O mesmo que o partitation(), mas começa a proxurar o separador pela direita

# Busca e Contagem
input().count("sub") #Conta quantas vezes "sub" aparece
input().find("sub") #Procura "sub" e retorna a posição (indice). Se não achar retorna -1
input().rfind("sub") #Mesmo que find, mas começa pela direita
input().index("sub") #igual o find(), mas da um erro se não encontrar
input().rindex("Sub") #Mesmo que o index, mas começa pela direita

# Verificação de inicio e fim
input().startswith("pre") # Se o começo comecar com "pre" = true
input().endswith("suf") # Se o fim começar com "suf" = True

# Alinhamento e preencimento 
input().center(largura) #Centraliza a string dentro de um espaço de largura total
input().ljust(largura) # Alinha string a esquerda (left-justify)
input().rjust(largura) # Alinha string a direita (right - justify)
input().zfill(largura) # Preenche a string com 0 a esquerda até atingir a largura "7".zfill(3) "007"
input().expandtabs() # Converte caracteres de tabulação \t em espaço

# Subistituição e Junção
input().replace("antigo", "novo") # Reescreve onde tiver "antigo", escreve o "novo" por cima
#Usar com csv?
input().join(lista) # Voce usa ele de forma inversa ao split, você junta uma lista. Exe: "-",join(['a','b','c']) -> "a-b-c" 