# While - While

quantidade_linhas = 5
quantidade_colunas = 5

linha = 1
coluna = 1

while linha <= quantidade_linhas:
  
  while coluna <= quantidade_colunas:
    print(f'[{linha} {coluna}]')
    
    coluna += 1
    
  linha += 1
  
print('Acabou')