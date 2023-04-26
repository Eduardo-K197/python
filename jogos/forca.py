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


def score_shot_kick():  # marcar chute certo
    position = 0
    for letter in secret_word:  # letra
        if shot == letter:
            right_letters[position] = letter
        position += 1


def draw_forca(erro, attempts, chance):  # draw_forca
    print("  _______     ")
    print(" |/      |    ")

    if not attempts > (chance + 1):
        if erro == 1:
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if erro == 2:
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if erro == 3:
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if erro == 4:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if erro == 5:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if erro == 6:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if erro == 7:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")
    else:
        print(" |            ")
        print("_|___         ")
        print()


opening_message()
secret_word = generate_secret_word().strip()  # palavra secreta

right_letters = starting_right_letters(secret_word)  # letras acertadas
print(right_letters)

attempts = 0  # tentativas
hit = False  # acertou
hanged = False  # enforcou
error = 0
chance = len(secret_word)


def victory():
    print(f'{secret_word} você se salvou parabens!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


while not hit and not hanged:

    shot = input('Qual letra?').upper().strip()  # chute

    if shot in secret_word:
        score_shot_kick()
    else:
        error += 1
        attempts += 1
        draw_forca(error, attempts, chance)
    print(right_letters)

    if '_' not in right_letters:
        victory()
        hit = True
        break

    if attempts > (chance + 1) and error > 7:
        print(f'Você se enforcou a palavra era {secret_word}!')
        hanged = True
        break

print('Fim de jogo')
