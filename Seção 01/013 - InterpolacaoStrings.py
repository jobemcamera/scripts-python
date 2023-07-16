# Interpolação básica de strings

# s - string
# d e i - int
# f - float
# x e X - hexadecimal

nome = 'Jobe'
preco = 1000.6365
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %i é %04x' % (6565, 6565))