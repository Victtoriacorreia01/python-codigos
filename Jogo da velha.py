
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(item == jogador for item in linha):
            return True
    
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    
    return False


def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0
    
    print("Bem-vindo ao Jogo da Velha!")
    imprimir_tabuleiro(tabuleiro)
    
    while True:
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))
        
        if tabuleiro[linha][coluna] != " ":
            print("Essa casa já está ocupada. Tente novamente.")
            continue
        
        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1
        imprimir_tabuleiro(tabuleiro)
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
            break
        
        if jogadas == 9:
            print("Empate!")
            break
        
        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogo_da_velha()
