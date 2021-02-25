nome = input('Qual é o seu nome?')
idade = int(input('Qual é a sua idade?'))
python = input('Você é estudante de Python?').lower()
padrao, vip = 35.00, 60.00
if idade >= 18 and idade < 80 and python == 'sim':
    print('Você tem acesso ao clube, mas primeiro, qual opção de ingresso você deseja?\n')
    opcao = int(input('Opção 1: Entrada Padrão R$ 35,00.\nOpção 2: Entrada Vip R$60,00.\nOpção escolhida: '))
    print('Temos um surpresa pra você que esta estudando de Python *-* .Você recebeu 50% de desconto na sua entrada:')
    if opcao == 1:
        padrao = padrao / 2
        print('Valor atualizado para meu querido estudante de Python R${}.'.format(padrao))
    elif opcao == 2:
        vip = vip / 2
        print('Valor atualizado para meu querido estudante de Python R${}.'.format(vip))
    else:
        print('Opcao inválida meu querido!')
elif idade >= 18 and idade < 80 and python == 'nao':
    print('Você tem acesso ao clube, mas primeiro, qual opção de ingresso você deseja?\n')
    opcao = int(input('Opção 1: Entrada Padrão R$ 35,00.\nOpção 2: Entrada Vip R$60,00.\nOpção escolhida: '))
    if opcao == 1:
        print('Voce escolheu a primeira opção, e o valor é R${}.'.format(padrao))
    elif opcao == 2:
        print('Você escolheu a segunda opção, e o valor é de R${}.'.format(vip))
else:
    if python == 'sim':
        print('Que bom que você é um estudante de Python *-*')
    print('Você não tem idade suficiente para entrar no clube :( .\nMas fique tranquilo, falta apenas {} anos para isso!'.format(18 - idade))