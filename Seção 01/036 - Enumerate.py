# Enumerate

lista = ["Maria", "Helena", "Luiz"]

lista_enumerada = enumerate(lista)

print(next(lista_enumerada)) # vira uma tupla -> (0, 'Maria')

for item in lista_enumerada:
  print(item)
  
# se eu der print novamente, o enumerate se esgota.

print('-'*30)
# Agora eu crio enumerate na hora
for item in enumerate(lista):
  print(item)
  
print('-'*30)

lista_enumerada_lista = list(enumerate(lista)) # cria uma tupla
print(lista_enumerada_lista)

# lista_enumerada_lista = list(enumerate(lista, start=19)) # posso escolher o começo

print('-'*30)

# desempacotamento dentro do for
for item in enumerate(lista): 
  indice, nome = item
  print(indice, nome)
  
print('-'*30)

# desempacotamento no for
for indice, nome in enumerate(lista): 
  print(indice, nome)
  
print('-'*30)

for tupla_enumerada in enumerate(lista):
  print('For da tupla:')
  for valor in tupla_enumerada:
    print(f'\t{valor}')