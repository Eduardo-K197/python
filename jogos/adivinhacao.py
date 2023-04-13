import random

print('########################################')
print('Bem vindo ao jogo de adivinhação!')
print('########################################')

tentativa = 3
numbSecret = random.randint(1,10)

while tentativa > 0:

    print('Você tem {} de três tentativas!'.format(tentativa))

    tentativa = (tentativa - 1)

    numeroUsuario = input('Digite um número: ')

    if not numeroUsuario.isdigit():
        print('só aceitamos números')
        break

    numeroUsuario = int(numeroUsuario)

    acertou = numbSecret == numeroUsuario

    if tentativa == 0 and not acertou:
        print('O número correto era {} Você errou!'.format(numbSecret))
        break
    if acertou:
        print('Você acertou!')
        break
    else:
        if numeroUsuario > numbSecret:
            print('Você errou ! o número é menor')
        else:
            print('Você errou ! o número é maior')