# Utilizando o mesmo jogo do main.py porem agora com for
import random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = random.randrange(100)
total_tentativa = 3
rodada = 1

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
        print("Voce acertou!!!")
        break
    else:
        if maior:
            print("Voce errou! O seu chute foi MAIOR que o numero secreto")
        elif menor:
            print("Voce errou! O seu chute foi MENOR que o numero secreto")

print("Fim do jogo! Numero secreto: ", numero_secreto)