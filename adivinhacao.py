from random import randint

def jogar():
    
    welcome_message()

    min_number = 1
    max_number = 100
    points = 1000

    random_number = randint(min_number, max_number)

    print("Escolha seu nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil", end="\n")

    difficulty = int(input("Escolha do nível: "))

    tries = set_difficulty(difficulty)

    for round in range(1, tries + 1):

        remaining_tries = tries - round

        guess = input("Digite um número entre {} e {}: ".format(min_number, max_number))
        int_guess = int(guess)

        print("Você digitou o número:", int_guess)

        is_valid_number = check_valid_number(int_guess, min_number, max_number, remaining_tries)
        if not is_valid_number:
            continue
        else:
            acertou = int_guess == random_number
            maior = int_guess < random_number
            menor = int_guess > random_number

            if (acertou):
                print("Parabéns, você acertou!", "-> Número secreto: {}".format(random_number), end="\n")
                print("Fim de jogo! Pontuação final: {} pts".format(points))
                break
            else:
                if(menor):
                    print("Resposta errada, o número secreto é menor que o número digitado!", end="\n")
                elif(maior):
                    print("Resposta errada, o número secreto é maior que o número digitado!", end="\n")
                lost_points = abs(random_number - int_guess)
                points = points - lost_points
                print("Você tem mais {} tentativas!".format(remaining_tries), sep=" ")

    else:
        print("Você perdeu, o número era: {}!".format(random_number))
        print("Fim de jogo! Pontuação final: {} pts".format(points), end="\n")

def welcome_message():
    print("**************************************")
    print("***Vamos jogar: Adivinhe o número!!***")
    print("**************************************", end="\n")

def set_difficulty(difficulty):
    if(difficulty == 1):
        tries = 15
        print("Você terá {} tentativas\n".format(tries))
        return tries
    elif(difficulty == 2):
        tries = 10
        print("Você terá {} tentativas\n".format(tries))
        return tries
    elif(difficulty == 3):
        tries = 5
        print("Você terá {} tentativas\n".format(tries))
        return tries
    else:
        tries = 3
        print("Número não válido - nível 'Super Difícil' escolhido!\nVocê terá {} tentativas".format(tries), end="\n")
        return tries

def check_valid_number(int_guess, min_number, max_number, remaining_tries):
    if(int_guess < min_number or int_guess > max_number):
        print("Você pode apenas digitar números entre {} e {}\n".format(min_number, max_number))
        print("Você tem mais {} tentativas!\n".format(remaining_tries), sep=" ")
        return False 

if(__name__ == "__main__"):
    jogar()