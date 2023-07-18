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

# Outras formatações

# padding
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.48565656:.1f}')
print(f'{1000.48565656:,.1f}') # mostra a virgula para separar milhar
print(f'{1000.48565656:-,.1f}') # mostra o sinal negativo
print(f'{1000.48565656:+,.1f}') # mostra o sinal positivo
print(f'{1000.48565656:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}') # maiúsculo
print(f'O hexadecimal de 1500 é {1500:08x}') # minúsculo
print(f'{variavel!r}') # conversion flags - !r !s !a
