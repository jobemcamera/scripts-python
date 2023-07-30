# While - Break

condicao = True

while condicao:
  nome = input('Digite um nome ou sair: ')
  print(f'Nome: {nome}')
  
  if nome == 'sair':
    break

print('Acabou.')


contador = 0

while contador < 10:
  print(contador)
  contador += 1
  