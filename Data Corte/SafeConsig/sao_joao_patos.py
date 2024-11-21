from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import date, timedelta
import time
import shutil
import os

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

tempo1 = 1
tempo2 = 2
tempo5 = 5
tempo_download = 20
login = "NSILVA"
senha = "Ic@123!@#"
site = ("https://saojoaodospatos.safeconsig.com.br/safe")

elemento_user = '//*[@id="idLogin"]'
elemento_password = '//*[@id="senhaUsuario"]'
elemento_entrar = '//*[@id="loginButtom"]/span[2]'
elemento_avancar_mes = '//*[@id="scheduleEventosartemis"]/div[1]/div[1]/div/button[2]/span'

navegador.get(site)
navegador.maximize_window()
time.sleep(tempo2)

if navegador.find_element('xpath',elemento_user):
    navegador.find_element('xpath',elemento_user).send_keys(login)
else:
    print("Erro ao inserir o login")

time.sleep(tempo1)

if navegador.find_element('xpath', elemento_password):
    navegador.find_element('xpath', elemento_password).send_keys(senha)   
else:
    print("Erro ao inserir a senha")

time.sleep(tempo1)

if navegador.find_element('xpath', elemento_entrar):
    navegador.find_element('xpath', elemento_entrar).click()
else:
    print("Erro ao inserir ao logar")

time.sleep(tempo5)

if navegador.find_element('xpath', elemento_avancar_mes):
    navegador.find_element('xpath', elemento_avancar_mes).click()
else:
    print("Erro ao inserir ao logar")

time.sleep(tempo5)

# Localiza o elemento que contém "Data de Corte" e armazena seu texto em uma variável
elemento_data_corte = navegador.find_element('xpath', "//*[contains(text(), 'Data de Corte')]")
nome_data_corte = elemento_data_corte.text

print('A data corte é:', nome_data_corte)

time.sleep(tempo5)

#Data de Corte 


