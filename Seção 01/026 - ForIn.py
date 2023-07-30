# For / in

# For = sabemos a quantidade de repetições
texto = 'Python'

novo_texto = ''
for letra in texto:
  novo_texto += f'*{letra}'
  print(letra) 

print(novo_texto)
  
  
# While = não sabemos a quantidade de repetições
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#   senha_digitada = input(f'Sua senha ({repeticoes}x): ')
  
#   repeticoes += 1
  
# print(repeticoes)