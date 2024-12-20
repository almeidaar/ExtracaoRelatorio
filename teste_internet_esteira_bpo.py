from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import date, timedelta
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

site = 'https://www.speedtest.net/pt'
maximizar_tela = 2
espera = 1.5
testando_conexao = 20
botao_iniciar = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
resultado = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'


navegador.get(site)
navegador.maximize_window()
time.sleep(maximizar_tela)

try:
    navegador.find_element('xpath',botao_iniciar)
    navegador.find_element('xpath',botao_iniciar).click()

except:
    print("Não foi possível encontrar o botão 'Iniciar''.")

time.sleep(testando_conexao)

try:
    navegador.find_element('xpath',resultado)
    conexao = navegador.find_element('xpath',resultado).text
    time.sleep(espera)

except:
    print("Não foi possível coletar o resultado do teste.")

print("A internet está com ", conexao, " megas de download de internet.")

#Teste de velocidade encerrou


#Iniciando teste esteira BPO

elemento_user = '//*[@id="txtUsuario_CAMPO"]'
elemento_senha = '//*[@id="txtSenha_CAMPO"]'
elemento_entrar = '//*[@id="bbConfirmar"]'
elemento_esteira = '//*[@id="ctl00_rptTopMenuContainer_ctl02_HyperLink1"]'
elemento_propostas = '//*[@id="ctl00_rptTopMenuContainer_ctl02_rptSubMenuItem_ctl01_linkButtonMenu"]'
elemento_filtro = '//*[@id="ctl00_Cph_lnkFiltrar"]/button'
elemento_cpf = '//*[@id="ctl00_Cph_txtCPF_CAMPO"]'
elemento_buscar = '//*[@id="ctl00_Cph_bbAtualizar"]'

tempo = 2
tempo_busca = 10
login = "MCC335185"
senha = ";351&,~<"
bpo = ("https://front.meucashcard.com.br/WebAppBPOCartao/Login/ICLogin?ReturnUrl=%2FWebAppBPOCartao%2FPages%2FMenu%2FICMenu")
cliente = 51649050860



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

time.sleep(tempo)

try:
    navegador.find_element('xpath',elemento_esteira)
    navegador.find_element('xpath',elemento_esteira).click()

except: print ('Não foi possivel encontrar o elemento esteira.')

time.sleep(tempo)

try:
    navegador.find_element('xpath',elemento_propostas)
    navegador.find_element('xpath',elemento_propostas).click()

except: print ("Não foi possível encontrar o elemento propostas.")

time.sleep(tempo)

try: 
    navegador.find_element('xpath',elemento_filtro)
    navegador.find_element('xpath',elemento_filtro).click()

except: print('Não foi possível encontrar o elemento de filtro.')

time.sleep(tempo)

try:
    navegador.find_element('xpath',elemento_cpf)
    navegador.find_element('xpath',elemento_cpf).click()
    navegador.find_element('xpath',elemento_cpf).send_keys(cliente)

except: print ("Não foi possível preencher o CPF do cliente.")

time.sleep(tempo)

try:
    navegador.find_element('xpath',elemento_buscar)
    navegador.find_element('xpath',elemento_buscar).click()

except: print("Não foi possível buscar.")

print("Consulta na esteira está funcionando!")

