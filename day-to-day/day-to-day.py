import pandas as pd
import os
import time
import threading
import pygetwindow as gw
from datetime import datetime


# Função para obter o nome do aplicativo em foco
def get_window_title():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title
        else:
            return "N/A"
    except:
        return "N/A"


# Função para salvar a data, hora e nome do aplicativo no arquivo CSV
def salvar_data_hora_app():
    file_name = "csv/" + datetime.today().strftime('%Y-%m-%d') + ".csv"

    # Cria o arquivo CSV se ainda não existir
    if not os.path.exists(file_name):
        df = pd.DataFrame(columns=["Data", "Hora", "Aplicativo"])
        df.to_csv(file_name, index=False)

    while True:
        # Obtém a data, hora atual e nome do aplicativo em foco
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        aplicativo_em_foco = get_window_title()

        # Cria um novo DataFrame com os dados atuais
        novo_registro = pd.DataFrame({"Data": [data_hora_atual.split()[0]],
                                      "Hora": [data_hora_atual.split()[1]],
                                      "Aplicativo": [aplicativo_em_foco]})

        print(novo_registro)

        # Lê o arquivo CSV existente, concatena com o novo registro e salva novamente
        df = pd.read_csv(file_name)
        df = pd.concat([df, novo_registro], ignore_index=True)
        df.to_csv(file_name, index=False)

        # Aguarda 30s
        time.sleep(30)


if __name__ == "__main__":
    # Inicia as threads para salvar data/hora/aplicativo e monitorar tecla 'q'
    threading.Thread(target=salvar_data_hora_app).start()
