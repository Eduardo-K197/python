import random

print('########################################')
print('Bem vindo ao jogo de adivinhação!')
print('########################################')

def advinha(de, ate):
    numbSecret = random.randint(de,ate)

    numeroUsuario = float(input('Digite um número: '))

    acertou = numbSecret == numeroUsuario

    if acertou:
        print('Você acertou!')
        return 'true'
    else:
        if numeroUsuario > numbSecret:
            print('Você errou ! o número é menor')
        else:
            print('Você errou ! o número é maior')
        return 'false'

while advinha(1,10) == 'false':
    advinha(1,10)
