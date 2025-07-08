import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Caminho da pasta onde os arquivos foram criptografados
TARGET_DIR = os.path.join(os.environ["USERPROFILE"], "Documents")

# Mesma chave usada para criptografar (32 bytes)
KEY = b"SuperSecureKey123456789012345678"

# Extensão dos arquivos criptografados
ENCRYPTED_EXTENSION = ".quodlocked"

def decrypt_file(filepath):
    with open(filepath, 'rb') as f:
        encrypted_data = f.read()

    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    try:
        original_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    except ValueError:
        print(f"[!] Falha ao descriptografar (padding inválido): {filepath}")
        return

    original_filepath = filepath.replace(ENCRYPTED_EXTENSION, "")
    with open(original_filepath, 'wb') as f:
        f.write(original_data)

    os.remove(filepath)
    print(f"[✓] Arquivo restaurado: {original_filepath}")

def find_and_decrypt_files():
    total = 0
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(ENCRYPTED_EXTENSION):
                full_path = os.path.join(root, file)
                decrypt_file(full_path)
                total += 1
    return total

if __name__ == "__main__":
    print("=== DECRIPTADOR DE RANSOMWARE (PRIDE Security) ===\n")
    total = find_and_decrypt_files()
    print(f"\n[✓] Total de arquivos restaurados: {total}")
