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