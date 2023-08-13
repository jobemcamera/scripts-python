# Desempacotamento 

nomes = ['Jobe', 'Pedro', 'Rafael', 'Bia']
nome1, nome2, nome3, nome4 = nomes

print(nome1, nome2, nome3, nome4)

print('\n')
numeros = [1, 2, 3, 4]
numero_1, *resto = numeros
_, numero_2, *_ = numeros

print(f'numeros: {numeros}')
print(f'numero_1: {numero_1}')
print(f'numero_2: {numero_2}')
print(f'*resto: {resto}')