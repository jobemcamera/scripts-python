# Formatação de Strings f-strings

nome = 'Jobe Camera'
altura = 1.72
peso = 60.20
imc = peso / altura ** 2

mensagem = f'{nome} mede {altura:.2f}m e pesa {peso:.2f}kg. Seu IMC é de {imc:.2f}.'
print(mensagem)


# Formatação de Strings format

a = 'A'
b = 'B'
c = '1.1'

formato = '{} mede {:.2f}m e pesa {:.2f}kg. Seu IMC é de {:.2f}.'.format(nome, altura, peso, imc)
print(formato)

# Caso precise de mais chamadas do mesmo parâmetro, use os índices.
formato = '{0} mede {1:.2f}m e pesa {2:.2f}kg. Seu IMC é de {3:.2f}.'.format(nome, altura, peso, imc)
print(formato)

# Parâmetro nomeados. Se nomear um parâmetros, todos precisam ser nomeados.
formato = '{n} mede {h:.2f}m e pesa {p:.2f}kg. Seu IMC é de {imc:.2f}.'.format(n=nome, h=altura, p=peso, imc=imc)
print(formato)