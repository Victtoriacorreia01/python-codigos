import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Estou pensando em um número entre 1 e 100.")

    while True:
        tentativa = int(input("Tente adivinhar o número: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    adivinhe_o_numero()
