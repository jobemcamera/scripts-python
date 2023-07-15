# Conversão de tipos, coerção
# str, int, float, bool - tipos imutáveis e primitivos

print(1 + 1)

print('a' + 'b') # concatena duas strings

# print('1' + 1) # can only concatenate str (not "int") to str - tipagem dinâmica forte

print(int('1'), type(int('1'))) # coerção do tipo
print(float('1'), type(float('1'))) # coerção do tipo

print(float('1') + 1) 

print(str(11) + 'b') 

print(bool(' ')) # True
print(bool('')) # False