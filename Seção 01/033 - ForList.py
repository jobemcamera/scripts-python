# For em List

lista = ['Jobe', 'Pedro', 'Rafael', 'Bia']

indices = range(len(lista))
for indice in indices:
  print(indice, lista[indice])

print('\n')

for index, nome in enumerate(lista):
  print(index, nome)