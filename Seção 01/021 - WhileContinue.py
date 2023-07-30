# While - Continue

contador = 0 

while contador <= 10:
  contador += 1
  
  if contador == 5: # pula o número 5
    continue
  
  print(f'Contador: {contador}')
  
print('Acabou!')