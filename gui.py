# gui.py
import tkinter as tk

def mainwindow(encrypted_key):
    root = tk.Tk()
    root.title("PRIDE Security")
    root.geometry("600x400")
    root.configure(bg="black")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=600, height=400, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Título Principal
    canvas.create_text(300, 40, text="PRIDE Security", fill="white", font=("Helvetica", 28, "bold"))

    # Alerta Vermelho
    canvas.create_text(300, 100, text="SEUS ARQUIVOS FORAM CRIPTOGRAFADOS", fill="red", font=("Helvetica", 16, "bold"))
    canvas.create_text(300, 140, text="Esta é uma simulação feita pela PRIDE Security", fill="white", font=("Helvetica", 12))

    # Chave criptografada
    canvas.create_text(300, 200, text="Encrypted Key:", fill="white", font=("Arial", 12, "bold"))
    canvas.create_text(300, 230, text=encrypted_key, fill="white", font=("Courier", 10), width=500)

    # Contato
    canvas.create_text(300, 300, text="Entre em contato: test@pridesec.com", fill="white", font=("Helvetica", 12, "italic"))

    root.mainloop()
