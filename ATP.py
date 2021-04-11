from datetime import datetime  # módulo será utilizado pelo código da etapa 02 para revelar a idade do cliente

# etapa 01 parte A
print('Bem-vindo à loja de instrumentos musicais do Evandro Afonso Rodrigues! \n'
      'A maior loja do sul do Brasil especializada em Guitarras e Violões!')

# etapa 01 parte B
print('Para aprovação de sua compra à prazo faremos uma rápida análise de crédito através de algumas perguntas!\n')

cargo = input('Para continuar, informe seu cargo atual: ')
salario = float(input('Informe seu salário bruto atual em R$: '))
anoNasc = int(input('Informe o ano de seu nascimento: '))

# etapa 01 parte C
print('\nPor favor, confira os dados abaixo:')
print('Cargo atual {}, salário atual R${:.2f} e ano de nascimento {}'.format(cargo, salario, anoNasc))

# etapa 02 parte A
ano = datetime.now()
idade = ano.year - anoNasc

print('Sua idade é de {} anos'.format(idade))

# etapa 02 parte B
credito = salario * (idade / 1000) + 100  # calculo do crédito
print('Seu crédito é de: R${:.2f}'.format(credito))

# etapa 03 parte A
nome = 'Evandro Afonso Rodrigues'
quantLetras = len(nome)  # contador de letras do nome do dono da loja
primeiroNome = 'Evandro'
quantLetrasPrimeiro = len(primeiroNome)

# etapa 03 parte B
produto = input('Qual é o produto que será comprado? ')
precoProduto = float(input('Informe o preço do produto: '))

liberado = credito * 0.6  # cálculo porcentagem - 60% do crédito
liberado2 = credito * 0.9  # cálculo porcengatem - 60% a 90% do crédito

bloqueado = 0
desconto = 0

if precoProduto <= liberado:  # verificação da situação de crédito do cliente
    print('Liberado')
elif precoProduto <= liberado2:
    print('Liberado para parcelar em até 2 vezes')
elif precoProduto <= credito:
    print('Liberado Para parcelar em até 3 vezes')
else:
    print('Bloqueado')
    bloqueado = 1

# etapa 03 parte 3
if (not bloqueado):
    if (quantLetras < precoProduto < idade):
        desconto = quantLetrasPrimeiro
        print('O desconto foi de: R${}'.format(desconto))
        precoFinal = precoProduto - desconto
        print('Valor final com desconto: R$ {:.2f}'.format(precoFinal))
    else:
        print('Não há desconto')
