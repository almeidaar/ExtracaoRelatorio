from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd  # Importando a biblioteca pandas

# Lendo a planilha propostas.xlsx
df = pd.read_excel(r'C:\Users\Nicholas Silva\source\ExtracaoRelatorio\Dowload Documentos\propostas.xlsx')  # Certifique-se de que o caminho está correto
propostas = df['Nro_Propostas'].tolist()  # Convertendo a coluna em uma lista

# Verificando se a lista de propostas está vazia
if not propostas:
    print("A lista de propostas está vazia. Verifique o arquivo propostas.xlsx.")
    exit()  # Encerra o script se a lista estiver vazia

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

elemento_user = '//*[@id="txtUsuario_CAMPO"]'
elemento_senha = '//*[@id="txtSenha_CAMPO"]'
elemento_entrar = '//*[@id="bbConfirmar"]'
elemento_download = '//*[@id="ctl00_Cph_ucAnexarDocumento1_grdDocumentos_ctl01_lnkDowloadTodos"]'

tempo1 = 1
tempo2 = 2
login = "nsilva"
senha = "Amd1$1$2"
bpo = "https://pixcard.banksofttecnologia.com.br/AppCartao/Pages/Menu/ICMenu"

navegador.get(bpo)
navegador.maximize_window()
time.sleep(tempo2)

if navegador.find_element('xpath', elemento_user):
    navegador.find_element('xpath', elemento_user).send_keys(login)
else:
    print("Erro ao inserir o login")

if navegador.find_element('xpath', elemento_senha):
    navegador.find_element('xpath', elemento_senha).send_keys(senha)   
else:
    print("Erro ao inserir a senha")

if navegador.find_element('xpath', elemento_entrar):
    navegador.find_element('xpath', elemento_entrar).click()
else:
    print("Erro ao inserir ao logar")

# Loop para cada proposta na lista
for proposta in propostas:
    link_proposta = "https://pixcard.banksofttecnologia.com.br/AppCartao/Pages/EsteiraProcessos/ICPropostaDetalhes?prop=" + str(proposta)

    navegador.get(link_proposta)  # Constrói a URL com a proposta
    time.sleep(tempo1)

    if navegador.find_element('xpath', elemento_download):
        navegador.find_element('xpath', elemento_download).click()
    else:
        print(f"Erro ao inserir ao fazer download da proposta {proposta}")

    time.sleep(tempo2)

# Feche o navegador após o término do download
navegador.quit()