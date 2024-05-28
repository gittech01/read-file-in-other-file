import os
import pandas as pd

def get_data_dir():
    """
    Retorna o caminho da pasta 'data' relativo ao script atual.
    """
    return os.path.join(os.path.dirname(__file__), '..', 'data')

def get_csv_files(data_dir):
    """
    Retorna uma lista de caminhos de arquivos CSV na pasta especificada.
    
    :param data_dir: Caminho para a pasta onde os arquivos CSV estão armazenados.
    :return: Lista de caminhos completos dos arquivos CSV.
    """
    return [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.csv')]

def read_csv_files(file_paths):
    """
    Lê arquivos CSV e retorna uma lista de DataFrames.
    
    :param file_paths: Lista de caminhos completos dos arquivos CSV.
    :return: Lista de DataFrames lidos a partir dos arquivos CSV.
    """
    data_frames = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        data_frames.append(df)
    return data_frames

def print_data_frames(data_frames):
    """
    Imprime os primeiros registros de cada DataFrame na lista.
    
    :param data_frames: Lista de DataFrames a serem impressos.
    """
    for i, df in enumerate(data_frames):
        print(f'DataFrame {i + 1} de {len(data_frames)}:')
        print(df.head(), '\n')

def main():
    data_dir = get_data_dir()
    csv_files = get_csv_files(data_dir)
    data_frames = read_csv_files(csv_files)
    print_data_frames(data_frames)

if __name__ == '__main__':
    main()
import os
import json

def list_files(directory):
    """
    Lista todos os arquivos em um diretório.
    :param directory: Caminho para o diretório.
    :return: Lista de nomes de arquivos.
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def read_json_file(file_path):
    """
    Lê um arquivo JSON e retorna seu conteúdo.
    :param file_path: Caminho para o arquivo JSON.
    :return: Conteúdo do arquivo JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def read_all_json_files(directory):
    """
    Lê todos os arquivos JSON em um diretório e retorna seus conteúdos.
    :param directory: Caminho para o diretório contendo os arquivos JSON.
    :return: Lista de conteúdos dos arquivos JSON.
    """
    file_list = list_files(directory)
    json_contents = []
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        if file_path.endswith('.json'):
            json_contents.append(read_json_file(file_path))
    return json_contents

if __name__ == '__main__':
    # Caminho para a pasta 'data'
    data_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    
    # Ler todos os arquivos JSON na pasta 'data'
    all_json_data = read_all_json_files(data_directory)
    
    # Exibir o conteúdo lido
    for json_data in all_json_data:
        print(json.dumps(json_data, indent=4))
