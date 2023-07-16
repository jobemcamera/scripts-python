# Operadores in e not in
# Strings são iteráveis

nome = 'Jobe'
print(nome[2])

print('b' in nome)
print('f' in nome)
print('ob' in nome)

print(10 * '-')

print('b' not in nome)
print('f' not in nome)
print('ob' not in nome)

print(10 * '-')

encontrar = 'ob'
if encontrar in nome:
    print(f'"{encontrar}" existe em "{nome}"')
else:
    print(f'"{encontrar}" não existe em "{nome}"')