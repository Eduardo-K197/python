numero = int(input('Digite um número para saber se ele é par ou ímpar: '))

retorno = 'ímpar'

if numero % 2 == 0:
    retorno = 'par'
print('O número {} é {}'.format(numero,retorno))