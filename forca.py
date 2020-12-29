def jogar():

    print("*************************")
    print("***Vamos jogar: Forca!***")
    print("*************************")

    secret_word = "uol"

    gameover = False
    acertou = False

    while(not gameover and not acertou):

        unformatted_guess = input("Insira uma letra: ")

        guess = unformatted_guess.lower().strip()

        index = 0
        for letter in secret_word:
            if(letter.lower() == guess):
                print("A palavra secreta contém a letra {} na posição {}!".format(guess, index))
            index = index + 1

        print("Vish")

    print("Fim de jogo!!")

if(__name__ == "__main__"):
    jogar()

