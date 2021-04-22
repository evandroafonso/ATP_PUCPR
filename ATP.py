# módulo será utilizado pelo código da etapa 02 - parte B para revelar a idade do cliente
from datetime import datetime


def obter_limite():  # etapa 04 - parte A
    global idade
    # etapa 01 parte A - apresentação da loja
    print('--------------------------------------------------------------------')
    print('Bem-vindo à loja de instrumentos musicais do Evandro Afonso Rodrigues! \n'
          'A maior loja do sul do Brasil especializada em Guitarras e Violões!')
    print('--------------------------------------------------------------------')

    # etapa 01 parte B - verificação de informações do cliente
    print('Para aprovação de sua compra à prazo faremos uma rápida análise de crédito através de algumas perguntas!\n')

    cargo = input('Para continuar, informe seu cargo atual: ')
    salario = float(input('Informe seu salário bruto atual em R$: '))
    ano_nasc = int(input('Informe o ano de seu nascimento: '))

    # etapa 01 parte C - exibição das informações do cliente
    print('\nPor favor, confira os dados abaixo:')
    print('Cargo atual {}, salário atual R${:.2f} e ano de nascimento {}'.format(cargo, salario, ano_nasc))

    # etapa 02 parte A - exibição da idade do cliente
    ano = datetime.now()
    idade = ano.year - ano_nasc

    print('Sua idade é de {} anos'.format(idade))

    # etapa 02 parte B - calculo do limite
    limite = salario * (idade / 1000) + 100  # calculo do limite
    print('Seu crédito é de: R${:.2f}'.format(limite))

    # etapa 04 - parte 04 - cadastro de produtos conforme necessidade
    print('------------------------------------')
    qtde_produto = int(input('Quantos produtos deseja cadastrar? '))

    # condição de repetição para verificar limite e quantidade de cadastro de produtos
    soma = 0
    for n in range(0, qtde_produto):
        verificar_produto(limite)
        soma = soma + preco_produto
        sobra_limite = limite - soma

        if sobra_limite >= 0:
            print('Restam R${} em seu limite de compras'.format(sobra_limite))
        else:
            print('Seu limite foi ultrapassado.')
            break

    return limite


def verificar_produto(limite):  # etapa 04 - parte B
    global preco_produto, produto
    # etapa 03 parte A
    nome = 'Evandro Afonso Rodrigues'
    quant_letras = len(nome)  # contador de letras do nome do dono da loja
    primeiro_nome = 'Evandro'
    quant_letras_primeiro = len(primeiro_nome)

    # etapa 03 parte B

    produto = input('Qual é o produto que será comprado? ')
    preco_produto = float(input('Informe o preço do produto: '))
    print('------------------------------------')
    liberado = limite * 0.6  # cálculo porcentagem - 60% do crédito
    liberado2 = limite * 0.9  # cálculo porcengatem - 60% a 90% do crédito

    bloqueado = 0
    desconto = 0

    if preco_produto <= liberado:  # verificação da situação de crédito do cliente
        print('Liberado')
    elif preco_produto <= liberado2:
        print('Liberado para parcelar em até 2 vezes')
    elif preco_produto <= limite:
        print('Liberado Para parcelar em até 3 vezes')
    else:
        print('Bloqueado')
        bloqueado = 1

    # etapa 03 parte 3
    if not bloqueado:
        if quant_letras < preco_produto < idade:
            desconto = quant_letras_primeiro
            print('O desconto foi de: R${}'.format(desconto))
            ano_nasc = preco_produto - desconto
            print('Valor final com desconto: R$ {:.2f}'.format(ano_nasc))
        else:
            print('Não há desconto')
    return desconto


# etapa 04 - parte A
obter_limite()
