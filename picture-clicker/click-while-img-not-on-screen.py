import pyautogui
import time


def buscar_imagem():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('search.png')
            return x, y
        except TypeError:
            # Imagem não encontrada, continue clicando
            pyautogui.click()
            time.sleep(0.5)  # Pausa de 0.5 segundos


def main():
    posicao = buscar_imagem()
    print(f'Imagem encontrada em {posicao}')


if __name__ == '__main__':
    main()
