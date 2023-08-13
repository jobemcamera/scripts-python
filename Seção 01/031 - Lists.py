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
  
print('\n')

numeros = [10, 20, 30, 40]
print(numeros)
del numeros[2]
print(numeros)

numeros.append(50)
print(numeros)

numeros.pop()
print(numeros)

# Faça isso somente se a lista for pequena
numeros.pop(1)
print(numeros)

print('\n')

lista_numeros = [135, 56, 98, 34]
print(lista_numeros)

lista_numeros.insert(0, 5)
print(lista_numeros)

# Vai inserir na última posição mas vai ignorar o índice 10000
lista_numeros.insert(10000, 10)
print(lista_numeros)