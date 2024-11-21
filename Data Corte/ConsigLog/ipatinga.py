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
login = "NSILVA_PIX"
senha = "Ic@123!@#"
site = ("https://saec.consiglog.com.br/Login.aspx")

elemento_user = '//*[@id="txtLogin"]'
elemento_proximo = '//*[@id="Entrar"]'
elemento_password = '//*[@id="txtSenha"]'
elemento_entrar = '//*[@id="Entrar"]'
elemento_selecionar_ipatinga = '//*[@id="gvOrgao_imgEntrar_0"]'
elemento_data_corte = '//*[@id="body_Prazos_gvPrazos"]/tbody/tr/td[4]'

navegador.get(site)
navegador.maximize_window()
time.sleep(tempo2)

if navegador.find_element('xpath',elemento_user):
    navegador.find_element('xpath',elemento_user).send_keys(login)
else:
    print("Erro ao inserir o login")

time.sleep(tempo1)

if navegador.find_element('xpath', elemento_proximo):
    navegador.find_element('xpath', elemento_proximo).send_keys(senha)   
else:
    print("Erro ao inserir a senha")

time.sleep(tempo2)

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

if navegador.find_element('xpath', elemento_selecionar_ipatinga):
    navegador.find_element('xpath', elemento_selecionar_ipatinga).click
else:
    print("Erro ao selecionar Ipatinga")

time.sleep(tempo5)

if navegador.find_element('xpath', elemento_data_corte):
    nome_data_corte = elemento_data_corte.text
    print("Erro ao selecionar Ipatinga")

# Localiza o elemento que contém "Data de Corte" e armazena seu texto em uma variável


print('A data corte é:', nome_data_corte)

time.sleep(tempo5)

#Data de Corte 


