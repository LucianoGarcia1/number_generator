from random import randint
quantidade_valores = int(input('Qual é a quantidade de valores? '))
valor_min = int(input('Qual é o valor mínimo a ser sorteado? '))
valor_max = int(input('Qual é o valor máximo a ser sorteado? '))

def sortear():
    valores = []
    print('Sorteando...')
    for n in range(quantidade_valores):
        valores.append(randint(valor_min, valor_max))

    print('Valore(s) Sorteado(s) com sucesso!')
    return valores

if quantidade_valores == 1:
    print('O valor sorteado foi {}'.format(sortear()))
elif quantidade_valores > 1:
    print('Os valores sorteados foram {}'.format(sortear()))
else:
    print('Ocorreu um erro! A quantidade deve ser maior que zero.')