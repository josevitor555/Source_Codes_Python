from main import *
#MAIN - Chamando as funções

def showLines(str):
  print('-' * 40)
  print(str)
  print('-' * 40)

showLines('> Banco o Galego <')

#Dados da conta corrente
num_conta_corrente = 0
saldo_conta_corrente = 0

#Dados da conta poupança
num_conta_poupanca = 0
saldo_conta_poupanca = 0

#Limites por saque
limite_saque = 3000
limite_diario = 10000

#Criar conta
print('\nDados da conta corrente: ')
minha_contaCorrente = criar_conta('conta_corrente', '1234C', 2000)
print(minha_contaCorrente)

print('\nDados da conta poupança: ')
minha_contaPoupanca = criar_conta('conta_poupanca', '1234P', 1000)
print(minha_contaPoupanca)

#Depositando um valor na conta corrente
print(f'\nDepositando em conta corrente')
deposito_CC = creditar('conta_corrente', 1000)
print(deposito_CC)

#Depositando um valor na conta poupança
print(f'\nDepositando em conta poupança')
deposito_CP = creditar('conta_poupanca', 1000)
print(deposito_CP)

#Tranferir da conta corrente para a conta poupança
print(f'\nDados da transação')
transferir('conta_corrente', 'conta_poupanca', 1000)

#Juros aplicado à conta poupança
juros_aplicado = aplicar_juros(10)
print(juros_aplicado)

# Sacar com limites
resultado_saque = sacar_com_limites('conta_corrente', 5000, limite_saque, limite_diario)
print(resultado_saque)

# Verificar saldo após o saque
print(saldo())
