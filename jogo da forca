import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "computador", "desenvolvimento", "inteligencia"]

# Escolhe uma palavra aleatória da lista
palavra_aleatoria = random.choice(palavras)

# Converte a palavra escolhida em letras minúsculas
palavra_aleatoria = palavra_aleatoria.lower()

letras_adivinhadas = []

maxerros = 6

erros = 0

while True:
    # Exibe a palavra oculta com as letras adivinhadas
    palavra_oculta = ""
    for letra in palavra_aleatoria:
        if letra in letras_adivinhadas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"

    print("\nPalavra: " + palavra_oculta)

    if palavra_oculta == palavra_aleatoria:
        print("Parabéns! Você ganhou!")
        break

    letra = input("Digite uma letra: ").lower()

    if letra in letras_adivinhadas:
        print("Você já adivinhou essa letra. Tente novamente.")
        continue

    letras_adivinhadas.append(letra)

    if letra in palavra_aleatoria:
        print("Letra correta!")
    else:
        print("Letra incorreta!")
        erros += 1

        if erros == maxerros:
            print("Você perdeu! A palavra era: " + palavra_aleatoria)
            break
