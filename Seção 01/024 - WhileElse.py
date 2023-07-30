# While - Else
# Após o while, o else é executado. Caso o laço seja quebrado (break), o else não é executado.

string = 'Valor qualquer'

i = 0

while i < len(string):
  letra = string[i]
  
  print(letra)
  i += 1

else:
  print('O else foi executado.')