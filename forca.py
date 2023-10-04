def jogar():

    print("*********************************")
    print("Bem vindo no jogo da forca!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas) #mostra ao usuario o tamanho da palavra que esta buscando

# enquanto nao enforocou e nao acertou, continua jogando
    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip() # utilizado para retirar espaço que o usuario poderia ter colocado

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f"Encontrei a letra {chute} na posicao {index}")
                letras_acertadas[index] = letra

            index = index + 1
        print(letras_acertadas)
        print("jogando....")


    print("Fim do jogo \n")

if(__name__ == "__main__"):
    jogar()