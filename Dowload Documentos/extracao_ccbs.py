import os
import zipfile
import shutil

# Diretórios
diretorio_zipados = r"C:\Users\Nicholas Silva\source\ExtracaoRelatorio\Dowload Documentos\DocumentosZipados"
diretorio_extraidos = r"C:\Users\Nicholas Silva\source\ExtracaoRelatorio\Dowload Documentos\DocumentosExtraidos"
diretorio_ccbs = r"C:\Users\Nicholas Silva\source\ExtracaoRelatorio\Dowload Documentos\CCBs"

# Função para extrair arquivos ZIP
def extrair_zip(diretorio_zipados, diretorio_extraidos):
    for arquivo in os.listdir(diretorio_zipados):
        if arquivo.endswith('.zip'):
            caminho_zip = os.path.join(diretorio_zipados, arquivo)
            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(diretorio_extraidos)
            print(f"Extraído: {arquivo}")

# Função para mover arquivos que contêm "Proposta"
def mover_propostas(diretorio_extraidos, diretorio_ccbs):
    for arquivo in os.listdir(diretorio_extraidos):
        if "Proposta" in arquivo:
            caminho_arquivo = os.path.join(diretorio_extraidos, arquivo)
            shutil.move(caminho_arquivo, diretorio_ccbs)
            print(f"Movido: {arquivo} para {diretorio_ccbs}")

# Executar as funções
extrair_zip(diretorio_zipados, diretorio_extraidos)
mover_propostas(diretorio_extraidos, diretorio_ccbs)

print("Processo concluído.")