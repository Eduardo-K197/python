print('########################################')
print('Bem vindo ao jogo de adivinhação!')
print('########################################')

def advinha():
    numbSecret = 49

    numbUser = int(input('Digite um número: '))

    acertou = numbSecret == numbUser

    if acertou:
        print('Você acertou!')
        return 'true'
    else:
        if numbUser < numbSecret:
            print('Você errou ! o número é menor')
        else:
            print('Você errou ! o número é maior')
        return 'false'

while advinha() == 'false':
    advinha()
