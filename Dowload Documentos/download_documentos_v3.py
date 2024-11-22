from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import date, timedelta
import time
import shutil
import os
import pandas as pd  # Importando a biblioteca pandas

# Lendo a planilha propostas.xlsx
df = pd.read_excel(r'C:\Users\Nicholas Silva\source\ExtracaoRelatorio\Dowload Documentos\propostas.xlsx')  # Certifique-se de que o caminho está correto
propostas = df['Nro_Propostas'].tolist()  # Convertendo a coluna em uma lista

# Verificando se a lista de propostas está vazia
if not propostas:
    print("A lista de propostas está vazia. Verifique o arquivo propostas.xlsx.")
    exit()  # Encerra o script se a lista estiver vazia

# Você pode escolher uma proposta específica, por exemplo, a primeira
proposta = propostas[0]  # Altere o índice conforme necessário

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

elemento_user = '//*[@id="txtUsuario_CAMPO"]'
elemento_senha = '//*[@id="txtSenha_CAMPO"]'
elemento_entrar = '//*[@id="bbConfirmar"]'
elemento_relatorios = '//*[@id="ctl00_rptTopMenuContainer_ctl05_HyperLink1"]'
elemento_rltr_analitico = '//*[@id="ctl00_rptTopMenuContainer_ctl05_rptSubMenuItem_ctl02_linkButtonMenu"]'
elemento_rltr_mov = '//*[@id="ctl00_Cph_rblTipoConsulta_1"]'
elemento_rltr_data1 = '//*[@id="ctl00_Cph_ucFaixaData_txtFaixaData_edit1_CAMPO"]'
elemento_rltr_data2 = '//*[@id="ctl00_Cph_ucFaixaData_txtFaixaData_edit2_CAMPO"]'
elemento_exportar = '//*[@id="ctl00_Cph_bbExportarCSV"]'
elemento_tirarBanner = '//*[@id="ctl00_Cph_bbHome"]'
elemento_esteira = '//*[@id="ctl00_rptTopMenuContainer_ctl02_HyperLink1"]'
elemento_propostas = '//*[@id="ctl00_rptTopMenuContainer_ctl02_rptSubMenuItem_ctl01_linkButtonMenu"]'
elemento_filtro = '//*[@id="ctl00_Cph_lnkFiltrar"]/button'
elemento_nro_proposta = '//*[@id="ctl00_Cph_txtNumeroProposta_CAMPO"]'
elemento_download = '//*[@id="ctl00_Cph_ucAnexarDocumento1_grdDocumentos_ctl01_lnkDowloadTodos"]'


tempo1 = 1
tempo2 = 2
tempo_download = 30
login = "nsilva"
senha = "Amd1$1$2"
bpo = ("https://pixcard.banksofttecnologia.com.br/AppCartao/Pages/Menu/ICMenu")
link_proposta = ("https://pixcard.banksofttecnologia.com.br/AppCartao/Pages/EsteiraProcessos/ICPropostaDetalhes?prop=", proposta)

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

navegador.get(link_proposta[0] + str(proposta))  # Constrói a URL com a proposta

time.sleep(tempo1)

if navegador.find_element('xpath', elemento_download):
    navegador.find_element('xpath', elemento_download).click()
else:
    print("Erro ao inserir ao fazer download")

time.sleep(tempo2)