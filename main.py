print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = "43"

chute = input("Digite o seu numero: ")

print("Voce digitou ", chute)

if chute > numero_secreto:
    print("Voce errou! seu numero foi maior que o numero secreto")
    print("A resposta era ", numero_secreto)

if chute < numero_secreto:
    print("Voce errou! seu numero foi menor que o numero secreto")
    print("A resposta era ", numero_secreto)

if chute == numero_secreto:
    print("Voce acertou!!!")
