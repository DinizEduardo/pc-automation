from datetime import datetime

import cv2
import os
import numpy as np


def criar_video(imagens, nome_video, fps, qualidade):
    altura_desejada = 720
    largura_desejada = 1280

    quarto = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(nome_video, quarto, fps, (largura_desejada, altura_desejada))

    for imagem_path in imagens:
        img = cv2.imread(imagem_path)

        # Obter as dimensões da imagem original
        altura_original, largura_original, _ = img.shape

        # Calcular a proporção de redimensionamento
        proporcao = min(largura_desejada / largura_original, altura_desejada / altura_original)

        # Calcular as novas dimensões mantendo a proporção de aspecto
        nova_largura = int(largura_original * proporcao)
        nova_altura = int(altura_original * proporcao)

        # Redimensionar a imagem para as novas dimensões com interpolação Lanczos
        img_redimensionada = cv2.resize(img, (nova_largura, nova_altura), interpolation=cv2.INTER_LANCZOS4)

        # Calcular as bordas para centralizar a imagem
        borda_vertical = (altura_desejada - nova_altura) // 2
        borda_horizontal = (largura_desejada - nova_largura) // 2

        # Criar uma imagem preta com as dimensões desejadas
        img_final = np.zeros((altura_desejada, largura_desejada, 3), dtype=np.uint8)

        # Preencher a região central com a imagem redimensionada
        img_final[borda_vertical:borda_vertical+nova_altura, borda_horizontal:borda_horizontal+nova_largura] = img_redimensionada

        video.write(img_final)

    video.release()
    cv2.destroyAllWindows()


def main():
    # Diretório das imagens
    diretorio_imagens = './photos'

    # Obter lista de imagens no diretório
    imagens = [os.path.join(diretorio_imagens, nome_arquivo) for nome_arquivo in os.listdir(diretorio_imagens) if
               nome_arquivo.endswith('.jpg')]

    duracao_desejada = 60  # em segundos

    # Calcular o FPS com base na quantidade de imagens e na duração desejada
    fps = len(imagens) / duracao_desejada

    # Configurar nome, FPS e qualidade do vídeo
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    nome_video = f'./videos/{data_hoje}_video.mp4'
    qualidade = cv2.VideoWriter_fourcc(*'mp4v')

    # Criar o vídeo
    criar_video(imagens, nome_video, fps, qualidade)


if __name__ == '__main__':
    main()
