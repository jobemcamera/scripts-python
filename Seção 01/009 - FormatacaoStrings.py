# Formatação de Strings f-strings

nome = 'Jobe Camera'
altura = 1.72
peso = 60.20
imc = peso / altura ** 2

mensagem = f'{nome} mede {altura:.2f}m e pesa {peso:.2f}kg. Seu IMC é de {imc:.2f}.'
print(mensagem)