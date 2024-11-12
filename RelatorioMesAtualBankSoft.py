from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import date, timedelta
import time
import shutil
import os

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

tempo1 = 1
tempo2 = 2
tempo_download = 30
login = "nsilva"
senha = "Amd1$1$2"
bpo = ("https://pixcard.banksofttecnologia.com.br/AppCartao/Pages/Menu/ICMenu")
data_atual = date.today()
data_atual_txt = data_atual.strftime('%d/%m/%y')

# Definindo o primeiro dia do mês
data_inicio_mes = date(data_atual.year, data_atual.month, 1)
data_inicio_mes_txt = data_inicio_mes.strftime('%d/%m/%y')

# data_inicio_mes = data_atual - timedelta(days=3)
# data_inicio_mes_txt = data_inicio_mes.strftime('%d/%m/%y')

navegador.get(bpo)
navegador.maximize_window()
time.sleep(tempo2)

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

if navegador.find_element('xpath', elemento_tirarBanner):
    navegador.find_element('xpath', elemento_tirarBanner).click()
else:
    print("Erro ao inserir ao logar")

time.sleep(tempo2)

if navegador.find_element('xpath',elemento_relatorios):
    navegador.find_element('xpath',elemento_relatorios).click()
else:
    print("Erro ao acessar os relatórios")

time.sleep(tempo1)

if navegador.find_element('xpath',elemento_rltr_analitico):
    navegador.find_element('xpath',elemento_rltr_analitico).click()
else:
    print("Erro ao acessar o relatório analítico")

time.sleep(tempo1)

if navegador.find_element('xpath',elemento_rltr_mov):
    navegador.find_element('xpath',elemento_rltr_mov).click()
else:
    print("Erro ao selecionar a opção de Movimentação")

time.sleep(tempo1)

if navegador.find_element('xpath',elemento_rltr_data1):
    navegador.find_element('xpath',elemento_rltr_data1).clear()
    navegador.find_element('xpath',elemento_rltr_data1).send_keys(data_inicio_mes_txt)
else:
    print("Erro ao inserir data de início")

time.sleep(tempo1)

if navegador.find_element('xpath',elemento_rltr_data2):
    navegador.find_element('xpath',elemento_rltr_data2).clear()
    navegador.find_element('xpath',elemento_rltr_data2).send_keys(data_atual_txt)
else:
    print("Erro ao inserir data final")

time.sleep(tempo1)

if navegador.find_element('xpath',elemento_exportar):
    navegador.find_element('xpath',elemento_exportar).click()
else:
    print("Erro ao exportar CSV")

print("Relatório Analítico extraído e funcionando!")

time.sleep(tempo_download)

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