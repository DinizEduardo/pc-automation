import csv
import os
from collections import Counter
import matplotlib.pyplot as plt
import datetime
import glob


def get_most_recent_csv():
    # Pasta onde os arquivos CSV estão localizados
    csv_folder = 'csv/'

    # Lista todos os arquivos .csv na pasta
    csv_files = glob.glob(os.path.join(csv_folder, "*.csv"))

    # Se não houver arquivos CSV, retorne None
    if not csv_files:
        return None

    # Função para extrair a data do nome do arquivo CSV
    def extract_date_from_filename(filename):
        try:
            # O padrão assume que o nome do arquivo tem o formato "YYYY-MM-DD.csv"
            base_filename = os.path.basename(filename)
            parts = base_filename.split("-")
            if len(parts) == 3:
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2].split(".")[0])
                return datetime.date(year, month, day)
        except ValueError:
            pass
        return None

    # Encontre o arquivo CSV com a data mais recente
    most_recent_date = None
    most_recent_csv = None
    for csv_file in csv_files:
        date = extract_date_from_filename(csv_file)
        if date:
            if most_recent_date is None or date > most_recent_date:
                most_recent_date = date
                most_recent_csv = csv_file

    return most_recent_csv


def count_repeated_phrases(filename):
    phrase_counts = Counter()

    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header if there is one

        for row in reader:
            if len(row) >= 2:  # Make sure there's at least a second column
                phrase = row[2]  # Get the whole phrase from the second column
                phrase_counts.update([phrase])  # Update the counter with the phrase in this row

    return phrase_counts


def main():
    # Obter o arquivo CSV mais recente
    csv_filename = get_most_recent_csv()

    if csv_filename is None:
        print("Nenhum arquivo CSV encontrado. O programa será encerrado.")
        return

    phrase_counts = count_repeated_phrases(csv_filename)

    # Ordenar as frases pela contagem decrescente
    sorted_phrases = sorted(phrase_counts.items(), key=lambda item: item[1], reverse=True)

    # Preparar dados para o gráfico de pizza (apenas os 15 primeiros valores)
    top_phrases = sorted_phrases[:15]
    labels = [phrase for phrase, _ in top_phrases]
    sizes = [count for _, count in top_phrases]

    # Criar o gráfico de pizza
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Para garantir que o gráfico seja um círculo

    plt.title('15 aplicativos mais usados.')

    # Obter a data atual no formato 'ano-mes-dia'
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")

    # Nome do arquivo CSV para salvar
    output_folder = 'compilado/'
    output_filename = os.path.join(output_folder, f"{date_str}-compilado.csv")

    # Salvar as 15 frases mais usadas em um arquivo CSV
    with open(output_filename, 'w', newline='', encoding='utf-8') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['Frase', 'Contagem'])  # Escrever o cabeçalho
        writer.writerows(top_phrases)

    # plt.show()


if __name__ == "__main__":
    main()
