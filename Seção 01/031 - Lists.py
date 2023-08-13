# Listas em Python
# Tipo list - mutável
# Métodos úteis: append, insert, pop, del, clear, extend...

lista_1 = list()
print(bool(lista_1)) # False

lista = ['Jobe', True, 1565, 6.89, []]
print(lista)

lista[1] = False

for index, item in enumerate(lista):
  print(f'item {index}: {item}, tipo: {type(item)}')