import sys

operacao = input('Digite a operação: ').split()
n1 = operacao[1]
n2 = operacao[2]
operacao = operacao[0]

if not n1.replace('.','').isdigit() and not n1.replace('.','').isdigit():
    print('Numero iválido')
    sys.exit(1)

n1 = float(n1)
n2 = float(n2)

dic = {'soma': f'{n1+n2}',
        'divisao': f'{n1/n2}',
        'multiplicacao': f'{n1*n2}',
        'subtracao': f'{n1-n2}'}

if operacao in dic:
    print(f'Resultado = {dic[operacao]}')
else:
    print('Operação inválida')
