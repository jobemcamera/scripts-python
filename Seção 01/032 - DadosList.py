# Cuidados com dados mutáveis
# copiado o valor (imutáveis)
# aponta para o mesmo valor da memória (mutável)

lista_a = ['Jobe', 'Rafael']
lista_b = lista_a

lista_a[0] = 'Outro nome'
# lista_b também é alterado
print(lista_b)


lista_c = [1, 2]
lista_d = lista_c.copy()

lista_c[0] = 0
# lista_d não é alterado
print(lista_d)