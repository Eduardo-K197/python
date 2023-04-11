print('########################################')
print('Bem vindo ao jogo de adivinhação!')
print('########################################')

numbSecret = 49

numbUser = input('Digite um número: ')

if numbSecret == int(numbUser):
    print('Você acertou!')
else:
    print('Você errou!')