# Iterável -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador 

texto1 = 'Jobe'.__iter__()
print(texto1)

texto2 = iter('Camera')
print(texto2)

texto3 = iter('Moraes')
print(texto3.__next__())
print(texto3.__next__())
print(next(texto3))
print(texto3.__next__())
print(texto3.__next__())
print(texto3.__next__())
# print(texto3.__next__()) aqui daria erro porque acabou a iteração

print(15 * '-')
# Como funciona o for por baixo dos panos...
# for letra in texto4
texto4 = 'Python'
iterador = iter(texto4)

while True:
  try:
    letra = next(iterador)
    print(letra)
  except StopIteration: # tratando o erro específico (StopIteration)
    break