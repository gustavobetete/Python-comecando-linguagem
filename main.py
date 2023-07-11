print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 43

chute_str = input("Digite o seu numero: ")

print("Voce digitou ", chute_str)

chute = int(chute_str)

if chute > numero_secreto:
    print("Voce errou! O seu chute foi MAIOR que o numero secreto")

if chute < numero_secreto:
    print("Voce errou! O seu chute foi MENOR que o numero secreto")

if chute == numero_secreto:
    print("Voce acertou!!!")

print("Fim do jogo")