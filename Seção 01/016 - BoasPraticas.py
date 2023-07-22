# Boas práticas
# Constante = 'Variáveis' que não vão mudar

velocidade = 65     # velocidade atual do carro
local_carro = 101   # local em que o carro está na estrada

# Variáveis que não vão mudar (maiúsculo)
RADAR_1 = 60      # velocida máxima do radar 1
LOCAL_1 = 100     # local onde o radar 1 está
RADAR_RANGE = 1   # a distância onde o radar pega

# Código complexo
if velocidade > RADAR_1 and local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
  print('Multado')
else:
  print('Não multado')
  
print(20 * '-')

# Código mais legível
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1 and carro_multado_radar_1:
  print('Multado')
else:
  print('Não multado')