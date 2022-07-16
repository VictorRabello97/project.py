# O Objetivo desse código é auxiliar os funcionários de RH de uma Empresa na hora de calcular o salário do funcionário.
# Levando em consideração que os descontos obrigatório na folha de pagamento são:

# 1 - Imposto de Renda (11%)
# 2 - INSS (8%)
# 3 - Sindicato (5%)
# 4 - Possiveis faltas.
# Ao final do programa, ele irá mostrar o valor do Salário bruto do funcionário,
# Todos os descontos listados com seus respectivos nomes e porcentagem e o calculo de faltas já acrescentado o DSR.

salario = float((input('Qual o salário do funcionário? ')).strip())
falta = str((input('O Funcionário possui alguma falta não justificada? \n 1 = Não \n 2 = Sim \n Resposta: ')).strip())
soma_das_faltas = 0

if falta == '2':
    quantidade_de_faltas = int((input('Quantas faltas o funcionário teve? \n Resposta: ')).strip())
    semanas = input("As faltas foram na mesma semana? \n 1 = SIM \n 2 = NAO \n Resposta: ")
    if semanas == '2':
        quantidade_de_semanas = int(input('As faltam ocorreram em quantas semanas distintas? \n Resposta: '))
        soma_das_faltas = salario / 30 * quantidade_de_faltas * quantidade_de_semanas

    else:
        soma_das_faltas = salario / 30 * quantidade_de_faltas


def calculo_de_descontos():
    calculos = dict()
    calculos['bruto'] = salario
    calculos['inss'] = calculos['bruto'] * 8 / 100
    calculos['sindicato'] = calculos['bruto'] * 5 / 100
    calculos['ir'] = calculos['bruto'] * 11 / 100
    calculos['faltas'] = soma_das_faltas
    calculos['descontos'] = calculos['inss'] + calculos['ir'] + calculos['sindicato'] + calculos['faltas']
    calculos['total_liquido'] = calculos['bruto'] - calculos['descontos']
    return calculos  # calculos tem várias 'variáveis' dentro dela. Vc está retornando todas essas váriaveis quando
    # executa ela


def mostrando_salario(bruto, inss, sindicato, ir, faltas, descontos, total_liquido):
    print("O Sálario do funcionário é: R$ {}".format(bruto))
    print("O Imposto de Renda retido, totalizou: R$: {} (11%)".format(ir))
    print("O INSS retido totalizou: R$ {} (8%)".format(inss))
    print("O Valor pago ao Sindicato totalizou: R$ {} (5%)".format(sindicato))
    print("O total de descontos no Salário do funcionário foi de R$: {}".format(descontos))
    print("O Total descontado de Falta + DSR foi de: R$: {}".format(faltas))
    print("O funcionário deverá receber: R$ {}".format(total_liquido))


total_descontos = calculo_de_descontos()  # agora todas as váriáeis que existiam dentro do dicionário calculos vão
# estar dentro da variavel valores

mostrando_salario(total_descontos['bruto'], total_descontos['inss'], total_descontos['sindicato'],
                  total_descontos['ir'], total_descontos['faltas'], total_descontos['descontos'],
                  total_descontos['total_liquido'])
# aqui preciso colocar os valores na ordem que vc definiu na hora de criar a função 'saida_dos_valores'