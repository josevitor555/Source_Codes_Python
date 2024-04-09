def criar_conta(tipo_conta, n_conta, saldo):
  global num_conta_corrente, saldo_conta_corrente, num_conta_poupanca, saldo_conta_poupanca

  match tipo_conta:
    case 'conta_corrente':
      num_conta_corrente = n_conta
      saldo_conta_corrente = saldo
      return f'>> {tipo_conta} {num_conta_corrente} foi criada com R$ {saldo_conta_corrente}'
    case 'conta_poupanca':
      num_conta_poupanca = n_conta
      saldo_conta_poupanca = saldo
      return f'>> {tipo_conta} {num_conta_poupanca} foi criada com R$ {saldo_conta_poupanca}'

def check_value(valor_passado):
  if valor_passado <= 0:
    print('>> Error: Insire um valor válido.')
    return False
  else:
    return True

def aplicar_juros(taxa):
  global saldo_conta_poupanca
  juros = taxa / 100 * saldo_conta_poupanca
  saldo_conta_poupanca = saldo_conta_poupanca + juros
  return f'>> Saldo da {num_conta_poupanca} é de {taxa}%: R$ {saldo_conta_poupanca}'

def sacar_com_limites(tipo_conta, valor_sacado, limite_saque, limite_diario):
  global saldo_conta_corrente, saldo_conta_poupanca, saldo_sacado_dia

  saldo_atual = saldo_conta_corrente if tipo_conta == 'conta_corrente' else saldo_conta_poupanca

  if not check_value(valor_sacado):
    return f'>> Error: Valor inválido.'

  match tipo_conta:
    case 'conta_corrente':
      if valor_sacado <= saldo_atual:
        if valor_sacado <= limite_saque:
          if (valor_sacado + saldo_sacado_dia) <= limite_diario:
            saldo_conta_corrente -= valor_sacado
            saldo_sacado_dia += valor_sacado
            return f'>> Valor sacado da conta corrente: R$ {valor_sacado}'
          else:
            return '>> Limite de saque diário excedido para a conta corrente.'
        else:
          return '>> Limite de saque por transação excedido para a conta corrente'
      else:
        return f'>> Saldo insuficiente para sacar R$ {valor_sacado} da conta corrente'
    case 'conta_poupanca':
      if valor_sacado <= saldo_atual:
        if valor_sacado <= limite_saque:
          if (valor_sacado + saldo_sacado_dia) <= limite_diario:
            saldo_conta_poupanca -= valor_sacado
            saldo_sacado_dia += valor_sacado
            return f'>> Valor sacado da conta poupança: R$ {valor_sacado}'
          else:
            return '>> Limite de saque diário excedido para a conta poupança.'
        else:
          return '>> Limite de saque por transação excedido para a conta poupança.'
      else:
        return f'>> Saldo insuficiente para sacar R$ {valor_sacado} da conta poupança.'
    case _:
      return '>> Tipo de conta inválida.'


def creditar(tipo_conta, valor_creditado):
  global saldo_conta_corrente, saldo_conta_poupanca

  if not check_value(valor_creditado):
    return f'>> Error: Valor inválido.'

  match tipo_conta:
    case 'conta_corrente':
      saldo_conta_corrente = saldo_conta_corrente + valor_creditado
      return f'>> Valor creditado para conta corrente: R$ {saldo_conta_corrente}'
    case 'conta_poupanca':
      saldo_conta_poupanca = saldo_conta_poupanca + valor_creditado
      return f'>> Valor creditado para conta poupança: R$ {saldo_conta_poupanca}'
    case _:
      return '>> Tipo de conta inválida!'

  return f'>> Saldo creditado: R$ {saldo_conta_corrente}'

def debitar(tipo_conta, valor_sacado):
  global saldo_conta_corrente, saldo_conta_poupanca

  if not check_value(valor_sacado):
    return f'>> Error: Valor inválido.'

  match tipo_conta:
    case 'conta_corrente':
      if (saldo_conta_corrente >= valor_sacado):
        saldo_conta_corrente = saldo_conta_corrente - valor_sacado
        return f'>> Valor sacado de {saldo_conta_corrente}: R$ {valor_sacado}'
    case 'conta_poupanca':
      if (saldo_conta_poupanca >= valor_sacado):
        saldo_conta_poupanca = saldo_conta_poupanca - valor_sacado
        return f'>> Valor sacado de {saldo_conta_poupanca}: R$ {valor_sacado}'
    case _:
        return '>> Tipo de conta inválida!'

  return f'>> Valor sacado: R$ {valor_sacado}'

def transferir(origem, destino, valor_transferido):
  match origem:
    case 'conta_corrente':
      debitar('conta_corrente', valor_transferido)
      creditar('conta_poupanca', valor_transferido)
    case 'conta_poupanca':
      debitar('conta_poupanca', valor_transferido)
      creditar('conta_corrente', valor_transferido)

def saldo():
  return f'>> Saldo atual de conta corrente: R$ {saldo_conta_corrente} e de conta poupança: R$ {saldo_conta_poupanca}'

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
