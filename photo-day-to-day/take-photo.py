import os
import cv2
from datetime import datetime, timedelta
import tkinter as tk
from tkinter.simpledialog import askfloat
from PIL import Image, ImageTk


class CapturaImagemApp:
    def __init__(self, root):
        self.root = root
        self.frame = None
        self.camera = None
        self.last_weight_date = self.get_last_weight_date()

        # Configurar janela em tela cheia
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='black')

        # Capturar imagem ao pressionar o botão
        self.botao_tirar = tk.Button(self.root, text='Tirar Foto', command=self.capturar_imagem)
        self.botao_tirar.pack()

        # Iniciar a câmera
        self.camera = cv2.VideoCapture(0)
        self.exibir_imagem()

        # Verificar se já se passaram 7 dias desde a última pesagem
        self.check_and_display_input()

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

        # Verificar se já se passaram 7 dias desde a última pesagem
        self.check_and_display_input()

    def check_and_display_input(self):
        if self.last_weight_date is None or (datetime.now() - self.last_weight_date).days >= 7:
            # Se passaram 7 dias ou é a primeira execução, mostrar input
            weight_input = askfloat("Informe o Peso", "Digite seu peso:")

            if weight_input is not None:
                # Atualizar arquivo de dados
                self.update_weight_file(weight_input)

    def update_weight_file(self, weight):
        # Gerar o nome do arquivo com a data atual
        data_atual = datetime.now().strftime("%Y-%m-%d")
        arquivo_path = os.path.join('photos', f'{data_atual}.txt')

        # Adicionar a data e peso ao arquivo
        with open(arquivo_path, 'a') as arquivo:
            arquivo.write(f"{data_atual};{weight}\n")

        # Atualizar a data da última pesagem
        self.last_weight_date = self.get_last_weight_date()

    def get_last_weight_date(self):
        # Obter o nome do único arquivo .txt na pasta 'photos'
        diretorio = 'photos'
        arquivos_txt = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.txt')]

        if len(arquivos_txt) == 1:
            # Se há exatamente um arquivo .txt, use o nome como data da última pesagem
            nome_arquivo = arquivos_txt[0]
            data_str = nome_arquivo.split('.')[0]  # Remover a extensão .txt
            return datetime.strptime(data_str, "%Y-%m-%d")
        else:
            # Se não houver nenhum ou mais de um arquivo, assuma que ainda não houve pesagem
            return None


def main():
    root = tk.Tk()
    app = CapturaImagemApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
