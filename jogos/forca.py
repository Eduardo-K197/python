print('########################################')
print('Bem vindo ao jogo da forca!')
print('########################################')

secret_word = 'abacate'  # palavra secreta
right_letters = ['_', '_', '_', '_', '_', '_', '_']  # letras acertadas

hit = False  # acertou
hanged = False  # enforcou

print(right_letters)

while not hit and not hanged:
    shot = input('Qual letra?').lower().strip()  # chute

    position = 0
    for letter in secret_word:  # letra
        if shot == letter:
            right_letters[position] = letter
        position += 1
    print(right_letters)
print('Fim de jogo')
