# Calcula o valor da compra de acordo com a forma de pagamento escolhida.
print('\033[31m{:^40}\033[m'.format('$$$$$ LOJAS ABERICANAS $$$$$'))
print(' ')
valor = float(input('Digite o valor da compra: R$ '))
print('Escolha uma forma de pagamento.')
forma = int(input('\033[31m[1]\033[m para pagamento à vista no dinheiro ou cheque.\n'
                  '\033[31m[2]\033[m à vista no cartão.\n'
                  '\033[31m[3]\033[m até 2x no cartão.\n'
                  '\033[31m[4]\033[m 3x ou mais no cartão.\n'
                  'Digite a opção: '))
print('\033[31m-+\033[m' * 65)
if forma == 1:
    total = valor - (valor * 10 / 100)
elif forma == 2:
    total = valor - (valor * 5 / 100)
elif forma == 3:
    total = valor
    vparcela = valor / 2
    print('Valor parcelado em 2x de R$ {} sem juros'.format(vparcela))
elif forma == 4:
    total = valor + (valor * 20 / 100)
    qparcela = int(input('Digite a quantidade de parcelas: '))
    if qparcela < 3:
       print('\033[4;31mATENÇÃO: Digite 3 ou mais parcelas.\033[m')
    else:
       vparcela = total / qparcela
       print('Valor parcelado em {}x de R$ {:.2f} com juros.'.format(qparcela, vparcela))
else:
    total = valor
    print('Escolha uma opção válida.')
print('Sua compra de {:.2f} ficará em {:.2f}'.format(valor, total))
