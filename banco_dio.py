print('------ Bem-vindo ao Nubielk! ------')

saldo = 0
limite = 500
numero_saques = 0
extrato = ''
LIMITE_SAQUES = 3

while True:
    escolha = input('[1. SACAR]'
                    '\n[2. DEPOSITAR]'
                    '\n[3. CONSULTAR EXTRATO]'
                    '\n[4. SAIR]'
                    '\nDigite sua escolha: ')
    
    if escolha == '2':
        valor = float(input('Informe o valor do depósito: R$'))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
            print('----------------------')
            print(f'Você depositou R${valor:.2f}')
            print('----------------------')

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif escolha == '1':
        valor = float(input('Informe o valor do saque: R$'))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite diário')

        elif excedeu_saques:
            print('Operação falhou! Você excedeu o número de saques diários.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            numero_saques += 1
            print('----------------------')
            print(f'Você sacou R${valor:.2f}')
            print('----------------------')

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif escolha == '3':
        print('\n************ EXTRATO ************')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('************************')

    elif escolha == '4':
        print('O banco Nubielk agradece a sua preferência!')
        break