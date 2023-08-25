import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


tamanho_senha = 12  
senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada:", senha_gerada)
