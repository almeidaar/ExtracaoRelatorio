from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import date, timedelta
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

bpo = ("https://front.meucashcard.com.br/WebAppBPOCartao/Login/ICLogin?ReturnUrl=%2FWebAppBPOCartao%2FPages%2FMenu%2FICMenu")
loginBPO = "MCC335185"
senhaBPO = ";351&,~<"

elemento_user = '//*[@id="txtUsuario_CAMPO"]'
elemento_senha = '//*[@id="txtSenha_CAMPO"]'
elemento_entrar = '//*[@id="bbConfirmar"]'
elemento_relatorios = '//*[@id="ctl00_rptTopMenuContainer_ctl05_HyperLink1"]'
elemento_rltr_analitico = '//*[@id="ctl00_rptTopMenuContainer_ctl05_rptSubMenuItem_ctl02_linkButtonMenu"]'
elemento_rltr_mov = '//*[@id="ctl00_Cph_rblTipoConsulta_1"]'
elemento_rltr_data1 = '//*[@id="ctl00_Cph_txtFaixaData_edit1_CAMPO"]'
elemento_rltr_data2 = '//*[@id="ctl00_Cph_txtFaixaData_edit2_CAMPO"]'
elemento_exportar = '//*[@id="ctl00_Cph_bbExportarCSV"]'

bucketS3 = ("https://us-east-1.console.aws.amazon.com/s3/buckets/mcc-app?region=us-east-1&bucketType=general&prefix=protected/leads/&showversions=false")
loginAWS = 'nsilva@meucashcard.com.br'
senhaAWS = 'Hbh4FARTD7HczUPrqL9n'

elemento_idAws = '//*[@id="account"]'
elemento_loginAws = '//*[@id="username"]'
elemento_senhaAws = '//*[@id="password"]'
elemento_entrarAWS = '//*[@id="signin_button"]'
elemento_carregarAws = '//*[@id="208-1714395653747-1028"]/div[1]/div[1]/div/div[1]/div/div[2]/span/div/div[9]/button'
elemento_adcArquivoAws = '//*[@id="141-1714396024079-4751"]/div[1]/div[1]/div/div[1]/div/div[2]/div/div[2]/button/span'


tempo = 2
tempo_download = 30


data_atual = date.today()
data_de_ontem = data_atual - timedelta(days=1) # Convert string back to date and subtract
data_ontem_txt = data_de_ontem.strftime('%d/%m/%Y')

data_finalDeSemana = data_atual - timedelta(days=3)
data_finalDeSemana_txt = data_finalDeSemana.strftime('%d/%m/%y')

print("Ontem foi dia: ", data_ontem_txt)
print("O final de semana começou no dia: ", data_finalDeSemana_txt)

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
    navegador.find_element('xpath',elemento_rltr_data1).send_keys(data_finalDeSemana_txt)
else:
    print("Erro ao inserir data de início")

if navegador.find_element('xpath',elemento_rltr_data2):
    time.sleep(tempo)
    navegador.find_element('xpath',elemento_rltr_data2).click()
    navegador.find_element('xpath',elemento_rltr_data2).clear()
    navegador.find_element('xpath',elemento_rltr_data2).send_keys(data_ontem_txt)
else:
    print("Erro ao inserir data final")

if navegador.find_element('xpath',elemento_exportar):
    time.sleep(tempo)
    navegador.find_element('xpath',elemento_exportar).click()
else:
    print("Erro ao exportar CSV")


time.sleep(tempo_download)
