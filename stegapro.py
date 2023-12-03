from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

# Função para esconder um arquivo em uma imagem
def esconder_arquivo(imagem_path, arquivo_path, imagem_saida_path):
    with open(arquivo_path, "rb") as arquivo:
        arquivo_binario = bytearray(arquivo.read())

    # Converter cada byte do arquivo para um caractere e adicionar à imagem
    imagem = Image.open(imagem_path)
    imagem_binario = bytearray(imagem.tobytes())

    # Certificar-se de que a bytearray da imagem seja grande o suficiente
    imagem_binario.extend([0] * (len(arquivo_binario) - len(imagem_binario)))

    for i in range(len(arquivo_binario)):
        imagem_binario[i] = (imagem_binario[i] & 254) | ((arquivo_binario[i] >> 7) & 1)

    imagem_de_saida = Image.frombytes(imagem.mode, imagem.size, bytes(imagem_binario))

    # Salvar a imagem resultante
    imagem_de_saida.save(imagem_saida_path)

# Função chamada quando o botão é pressionado
def on_button_click():
    imagem_path = filedialog.askopenfilename(title="Selecione a imagem")
    arquivo_path = filedialog.askopenfilename(title="Selecione o arquivo a esconder")
    imagem_saida_path = filedialog.asksaveasfilename(title="Salvar imagem resultante como")

    esconder_arquivo(imagem_path, arquivo_path, imagem_saida_path)
    resultado_label.config(text="Operação concluída com sucesso!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Esconder Arquivo em Imagem")

# Botão para iniciar o processo
button = tk.Button(root, text="Esconder Arquivo", command=on_button_click)
button.pack(pady=20)

# Rótulo para exibir o resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Executar a interface gráfica
root.mainloop()
