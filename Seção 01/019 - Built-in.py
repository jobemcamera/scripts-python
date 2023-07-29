# Tipos imbutidos no Python
# Imutáveis: str, int, float, bool

# Não posso mudar desse jeito
string = 'Jobe Camera'
# string[3] = 'ABC'
print(string[3])

# Posso mudar desse jeito, criando outra variável
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)

# Métodos de string
print(string.capitalize())

print(string.zfill(50))