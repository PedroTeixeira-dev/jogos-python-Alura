import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de adivinhacao!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)

    print("Qual nivel de dificuldade?")
    print("(1) Facil  (2) Medio  (3) Dificil")

    validado = 0
    pontos = 1000

    while(validado == 0):
        nivel = int(input("Escolha o nivel: "))

        if(nivel == 1):
            total_de_tentativas = 20
            validado = 1
        elif(nivel == 2):
            total_de_tentativas = 10
            validado = 1
        elif(nivel == 3):
            total_de_tentativas = 5
            validado = 1
        else:
            print("Voce deve escolher uma opcao valida")




    total = total_de_tentativas
    tentativa_atual = 1

    for rodada in range(1,total_de_tentativas + 1):

        print("tentativa {} de {}".format(tentativa_atual, total))
        tentativa_atual = 1 + tentativa_atual

        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Voce digitou :", chute)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            print("Voce errou")
            if(maior):
                print("Seu numero foi maior do que o numero secreto", "\n")
            elif(menor):
                print("Seu numero foi menor que o numero secreto", "\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        if(rodada == total_de_tentativas):
            print("O numero secreto era {}. Voce fex {} pontos".format(numero_secreto, pontos))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()