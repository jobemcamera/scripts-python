# Introdução ao try/except

numero_str = input('Digite um número: ')

try:
  numero_float = float(numero_str)
  print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
  print('Isso não é um número.')

# if numero_str.isdigit(): # Somente números (. não é número)
#   numero_float = float(numero_str)
#   print(f'O dobro de {numero_float} é {numero_float * 2}')
# else:
#   print('Isso não é um número.')