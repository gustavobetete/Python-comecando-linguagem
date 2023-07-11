print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 43
total_tentativa = 3
rodada = 1

while rodada <= total_tentativa:
    # print(f"Tentativa {rodada} de {total_tentativa}") Uma maneira de fazer
    print("Tentativa {} de {}".format(rodada, total_tentativa))
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

    rodada = rodada + 1
    if rodada > 3:
        print("Numero de tentativas excedidas...")
        break

print("Fim do jogo")