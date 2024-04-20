from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def Gerar_ParChaves():
    # Gera um novo par de chaves RSA de 2048 bits
    chave = RSA.generate(2048)
    return chave

def Encriptar_Mensagem(chave_publica, mensagem):
    # Cria um objeto de cifra usando a chave pública
    cipher = PKCS1_OAEP.new(chave_publica)
    # Criptografa a mensagem
    mensagem_criptografada = cipher.encrypt(mensagem.encode())
    return mensagem_criptografada

def Descriptografar_Mensagem(chave_privada, mensagem_encriptada):
    # Cria um objeto de cifra usando a chave privada
    cifra = PKCS1_OAEP.new(chave_privada)
    # Descriptografa a mensagem
    mensagem_descriptografada = cifra.decrypt(mensagem_encriptada)
    return mensagem_descriptografada.decode()

# Gerar um novo par de chaves
Par_Chaves = Gerar_ParChaves()
Chave_Publica = Par_Chaves.publickey()
Chave_Privada = Par_Chaves

# Mensagem a ser criptografada
Mensagem = "Escreva a mensagem aqui."

# Criptografar a mensagem usando a chave pública
Encriptada_Mensagem = Encriptar_Mensagem(Chave_Publica, Mensagem)

# Descriptografar a mensagem usando a chave privada
Descriptografada_Mensagem = Descriptografar_Mensagem(Chave_Privada, Encriptada_Mensagem)

# Exibir resultados
print("Mensagem original:", Mensagem)
print("Mensagem criptografada:", Encriptada_Mensagem)
print("Mensagem descriptografada:", Descriptografada_Mensagem)
