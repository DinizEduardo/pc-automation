import os

import cv2
from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk


class CapturaImagemApp:
    def __init__(self, root):
        self.root = root
        self.frame = None
        self.camera = None

        # Configurar janela em tela cheia
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='black')

        # Capturar imagem ao pressionar o botão
        self.botao_tirar = tk.Button(self.root, text='Tirar Foto', command=self.capturar_imagem)
        self.botao_tirar.pack()

        # Iniciar a câmera
        self.camera = cv2.VideoCapture(0)
        self.exibir_imagem()

    def exibir_imagem(self):
        # Ler o frame da câmera
        ret, frame = self.camera.read()

        # Converter o frame para o formato de imagem do Tkinter
        imagem = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imagem = Image.fromarray(imagem)
        imagem = ImageTk.PhotoImage(imagem)

        # Criar ou atualizar o widget de imagem
        if self.frame is None:
            self.frame = tk.Label(self.root, image=imagem)
            self.frame.pack()
        else:
            self.frame.configure(image=imagem)
            self.frame.image = imagem

        # Chamar esta função novamente após um intervalo para atualizar a imagem
        self.root.after(10, self.exibir_imagem)

    def capturar_imagem(self):
        # Ler o frame da câmera
        ret, frame = self.camera.read()

        # Gerar o nome do arquivo com data e hora
        nome_arquivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.jpg'

        # Diretório onde a imagem será salva
        diretorio = 'photos'

        # Criar o caminho completo do arquivo
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        # Certificar-se de que o diretório existe, se não, crie-o
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        # Salvar a imagem no diretório especificado
        cv2.imwrite(caminho_arquivo, frame)

        # Liberar a câmera
        self.camera.release()

        # Fechar a janela
        self.root.destroy()


def main():
    root = tk.Tk()
    app = CapturaImagemApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
