import random

def jogar_pedra_papel_tesoura():
    escolhas = ["pedra", "papel", "tesoura"]
    
    while True:
        escolha_computador = random.choice(escolhas)
    
        escolha_jogador = input("Escolha pedra, papel ou tesoura (ou sair para encerrar o jogo): ").lower()
        
        if escolha_jogador == "sair":
            print("Obrigado por jogar!")
            break
        
        if escolha_jogador not in escolhas:
            print("Escolha inválida. Tente novamente.")
            continue
        
        print("Computador escolheu:", escolha_computador)
        print("Jogador escolheu:", escolha_jogador)
        
        
        if escolha_jogador == escolha_computador:
            print("Empate!")
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra"):
            print("O jogador venceu!")
        else:
            print("Computador venceu!")

if __name__ == "__main__":
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    jogar_pedra_papel_tesoura()
