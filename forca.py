import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo da forca!")
    print("*********************************")

    arquivo =open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas) #mostra ao usuario o tamanho da palavra que esta buscando

# enquanto nao enforocou e nao acertou, continua jogando
    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper() # utilizado para retirar espaço que o usuario poderia ter colocado

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    print(f"Encontrei a letra {chute} na posicao {index}")
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, voce errou. Faltam {6 - erros} tentativas")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


    if(acertou):
        print('Voce ganhou !')
    else:
        print('Voce perdeu \n')
    print("Fim do jogo \n")

if(__name__ == "__main__"):
    jogar()