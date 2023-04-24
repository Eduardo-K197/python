import random

print('########################################')
print('Bem vindo ao jogo de adivinhação!')
print('########################################')

tentativa = 3
pontos = 100
nivel = int(input('''Em qual nível você deseja jogar?
          [0]Básico
          [1]Médio
          [2]Difícil

    Digite sua escolha: '''))

match nivel:
    case 0:
        tentativa = 8
    case 1:
        tentativa = 5
    case 2:
        tentativa = tentativa

numbSecret = random.randint(1, 10)

while tentativa > 0:

    print('Você tem {} tentativas e {} pontos!'.format(tentativa, pontos))

    numeroUsuario = input('Digite um número: ')

    # Validações

    if not numeroUsuario.isdigit():
        print('só aceitamos números')
        continue

    if float(numeroUsuario) < 0:
        print('E números positivos')
        continue

    numeroUsuario = int(numeroUsuario)

    tentativa -= 1

    # pontuação e resultado

    acertou = numbSecret == numeroUsuario

    if tentativa == 0 and not acertou:
        print('O número correto era {} Você errou!'.format(numbSecret))
        break
    if acertou:
        print(f'Você acertou! e com {pontos} pontos parabens!')
        break
    else:
        pontos -= 10
        if numeroUsuario > numbSecret:
            print('Você errou ! o número é menor perdeu 10 pontos')
            print('########################################')
        else:
            print('Você errou ! o número é maior perdeu 10 pontos')
            print('########################################')
