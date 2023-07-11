# Utilizando o mesmo jogo do main.py porem agora com for
import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativa = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativa = 20
    elif nivel == 2:
        total_tentativa = 10
    else:
        total_tentativa = 5

    for rodada in range(1, total_tentativa + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativa))

        chute_str = input("Digite um número de 1 a 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Digite um número válido entre 1 a 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Voce errou! O seu chute foi MAIOR que o numero secreto")
            elif menor:
                print("Voce errou! O seu chute foi MENOR que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo! Numero secreto: ", numero_secreto)

if __name__ == "__main__":
    jogar()