from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import date, timedelta
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


elemento_user = '//*[@id="txtUsuario_CAMPO"]'
elemento_senha = '//*[@id="txtSenha_CAMPO"]'
elemento_entrar = '//*[@id="bbConfirmar"]'
elemento_relatorios = '//*[@id="ctl00_rptTopMenuContainer_ctl05_HyperLink1"]'
elemento_rltr_analitico = '//*[@id="ctl00_rptTopMenuContainer_ctl05_rptSubMenuItem_ctl02_linkButtonMenu"]'
elemento_rltr_mov = '//*[@id="ctl00_Cph_rblTipoConsulta_1"]'
elemento_rltr_data1 = '//*[@id="ctl00_Cph_txtFaixaData_edit1_CAMPO"]'
elemento_rltr_data2 = '//*[@id="ctl00_Cph_txtFaixaData_edit2_CAMPO"]'
elemento_exportar = '//*[@id="ctl00_Cph_bbExportarCSV"]'

tempo = 2
tempo_download = 30
login = "MCC335185"
senha = ";351&,~<"
bpo = ("https://front.meucashcard.com.br/WebAppBPOCartao/Login/ICLogin?ReturnUrl=%2FWebAppBPOCartao%2FPages%2FMenu%2FICMenu")
data_inicial = "15/05/2024"
data_final = "15/05/2024"

navegador.get(bpo)
navegador.maximize_window()
time.sleep(tempo)

if navegador.find_element('xpath',elemento_user):
    navegador.find_element('xpath',elemento_user).send_keys(login)
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
          
if navegador.find_element('xpath',elemento_relatorios):
    time.sleep(tempo)
    navegador.find_element('xpath',elemento_relatorios).click()
else:
    print("Erro ao acessar os relatórios")

if navegador.find_element('xpath',elemento_rltr_analitico):
    time.sleep(tempo)
    navegador.find_element('xpath',elemento_rltr_analitico).click()
else:
    print("Erro ao acessar o relatório analítico")

if navegador.find_element('xpath',elemento_rltr_mov):
    time.sleep(tempo)
    navegador.find_element('xpath',elemento_rltr_mov).click()
else:
    print("Erro ao selecionar a opção de Movimentação")

if navegador.find_element('xpath',elemento_rltr_data1):
    time.sleep(tempo)
    navegador.find_element('xpath',elemento_rltr_data1).clear()
    navegador.find_element('xpath',elemento_rltr_data1).send_keys(data_inicial)
else:
    print("Erro ao inserir data de início")

if navegador.find_element('xpath',elemento_rltr_data2):
    time.sleep(tempo)
    navegador.find_element('xpath',elemento_rltr_data2).click()
    navegador.find_element('xpath',elemento_rltr_data2).clear()
    navegador.find_element('xpath',elemento_rltr_data2).send_keys(data_final)
else:
    print("Erro ao inserir data final")

if navegador.find_element('xpath',elemento_exportar):
    time.sleep(tempo)
    navegador.find_element('xpath',elemento_exportar).click()
else:
    print("Erro ao exportar CSV")

print("Relatório Analítico extraído e funcionando!")

time.sleep(tempo_download)
