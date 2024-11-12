import shutil
import os

# Definindo os caminhos
source = r"C:\Users\Nicholas Silva\Downloads\RelatorioProducaoAnalitico.CSV"
destination = r"C:\Users\Nicholas Silva\OneDrive - PIX CARD SERVICOS TECNOLOGICOS E FINANCEIROS LTDA\Área de Trabalho"

# Verificando se o arquivo existe
if not os.path.isfile(source):
    print(f"O arquivo não foi encontrado em: {source}")
else:
    print(f"O arquivo foi encontrado em: {source}")  # Adicione esta linha para depuração
    try:
        # Movendo o arquivo
        shutil.move(source, destination)
        print(f"Arquivo movido com sucesso para: {destination}")
    except PermissionError:
        print("Permissão negada. Verifique se você tem permissão para mover o arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")