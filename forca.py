import random

def jogar():

    print_game_title()
    secret_word = load_secret_word()

    guessed_letters = start_guessed_letter(secret_word)
    print(guessed_letters)

    gameover = False
    guessed = False
    errors = 0
    max_tries = 6

    while(not gameover and not guessed):

        guess = ask_for_guess()

        if(guess in secret_word):
            set_right_guess(secret_word, guessed_letters, guess)
        else:
            errors += 1
            set_wrong_guess(errors, max_tries)
            desenha_forca(errors)

        print(guessed_letters)

        gameover = errors > max_tries
        guessed = "_" not in guessed_letters

    call_end_game(guessed, secret_word)

def print_game_title():
    print("*************************")
    print("***Vamos jogar: Forca!***")
    print("*************************")

def load_secret_word():
    file = open("words.txt", "r")
    words = []
    for row in file:
        row = row.strip()
        words.append(row)
    file.close()

    random_word = random.randrange(0, len(words))
    secret_word = words[random_word].lower()

    return secret_word

def start_guessed_letter(secret_word):
    return ["_" for qty_letter in secret_word]

def ask_for_guess():
    unformatted_guess = input("Insira uma letra: ")
    guess = unformatted_guess.strip().lower()
    return guess

def set_right_guess(secret_word, guessed_letters, guess):
    index = 0
    for letter in secret_word:
        if(letter == guess):
            guessed_letters[index] = letter
            print("A palavra secreta contém a letra '{}' na posição {}!".format(guess, index + 1))
        index += 1

def set_wrong_guess(errors, max_tries):
    print("Vish, agora restam {} tentativas!".format(max_tries - errors))

def call_end_game(guessed, secret_word):
    if(guessed):
        print("Correto, você ganhou!! Palavra secreta: '{}'".format(secret_word))
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
    else:
        print("Que pena, você foi enforcado!")
        print("A palavra era '{}'".format(secret_word))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")   
    print("Fim de jogo!!")

def desenha_forca(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()