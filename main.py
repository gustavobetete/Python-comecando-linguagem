print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 43
total_tentativa = 3

while total_tentativa != 0:
    chute_str = input("Digite o seu numero: ")

    print("Voce digitou ", chute_str)

    chute = int(chute_str)

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

print("Fim do jogo")