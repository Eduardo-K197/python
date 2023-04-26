import random


def opening_message():  # mensagem de abertura
    print('########################################')
    print('Bem vindo ao jogo da forca!')
    print('Tema: Fruta!')
    print('######################################## \n')


def generate_secret_word():
    file = open('palavras.txt', 'r')
    words = []  # palavras

    for line in file:
        line = line.upper().strip()
        words.append(line)

    file.close()

    numb = random.randrange(0, len(words))
    secret_word = words[numb].upper()  # palavra secreta
    return secret_word


def starting_right_letters(word):  # iniciando letras acertadas
    return ['_' for letter in word]


opening_message()
secret_word = generate_secret_word()
right_letters = starting_right_letters(secret_word) # letras acertadas

attempts = 0  # tentativas
hit = False  # acertou
hanged = False  # enforcou

print(right_letters)

while not hit and not hanged:
    shot = input('Qual letra?').upper().strip()  # chute

    position = 0
    for letter in secret_word:  # letra
        if shot == letter:
            right_letters[position] = letter
        position += 1
    print(right_letters)

    if '_' not in right_letters:
        print(f'{secret_word} você acertou parabens!')
        hit = True
        break

    attempts += 1
    if attempts > (len(secret_word) + 1):
        print(f'Você Perdeu a palavra era {secret_word}!')
        hanged = True
        break

print('Fim de jogo')
