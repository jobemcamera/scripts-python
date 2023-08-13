# Tuplas (lista imutável) - se não for alterar a lista, trabalhe com tupla

nomes = ('Jobe', 'Pedro', 'Rafael', 'Bia')
print(nomes, type(nomes))

nomes = tuple(nomes)
print(nomes, type(nomes))

nomes = list(nomes)
print(nomes, type(nomes))