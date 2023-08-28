print("**************")
print("Bem Vindo ao jogo de adivinhção")
print("**************")

numerosecreto = 42
totaldetentativas = 3

for rodada in range(1, totaldetentativas + 1):
    print("tentativa {} de {}" .format(rodada, totaldetentativas))
    chuter = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou", chuter)
    chute = int(chuter)

    if(chute < 1 or chute > 100):
        print("Voce digitou errado, tente novamente")
        continue

    acertou = chute == numerosecreto
    maior = chute > numerosecreto
    menor = chute < numerosecreto

    if(numerosecreto == chute):
        print("Você acertou!")
        break
    else:
        if(chute > numerosecreto):
            print("Voce errou! o seu chute foi maior que o numero secreto")
        elif(chute < numerosecreto):
            print("Voce errou! o seu chute foi menor que o numero secreto")

print("FIM DO JOGO!")
