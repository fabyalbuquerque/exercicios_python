from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

navegador = webdriver.Chrome()

navegador.get(r"https://www.google.com/")


# Pesquisa

campo_pesquisa = navegador.find_element(By.XPATH, '//*[@id="APjFqb"]')
campo_pesquisa.clear()

campo_pesquisa.send_keys("Goiânia" + Keys.RETURN)

navegador.implicitly_wait(5)

link_wikipedia = navegador.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
link_wikipedia.click()


# Arquivo txt

conteudo_pagina = navegador.find_element(By.XPATH, '/html/body').text

with open("goiania_wikipedia.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_pagina)
    

# Arquivo img

link_imagem = navegador.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[1]/span/a/img').get_attribute('src')
imagem = requests.get(link_imagem).content


with open("bandeira_goiania.png", "wb") as arquivo_imagem:
    arquivo_imagem.write(imagem)
    

# Captura dos itens

linhas_tabela = navegador.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr')


itens = []

for linha in linhas_tabela:
    colunas_linha = linha.find_elements(By.TAG_NAME, 'td')
    
    if len(colunas_linha) != 2:
        continue
        
    chave = colunas_linha[0].text.strip()
    valor = colunas_linha[1].text.strip()

    itens.append((chave, valor))


# #Escrever conteudo HTML

html_conteudo = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabela - Goiânia - Wikipedia</title>
    </head>
    <body>
        <h1>Informações sobre Goiânia</h1>
        <img src="bandeira_goiania.png" alt="Bandeira Goiânia">"""

lista = ""

for chave, valor in itens: 
    lista += f"<li><strong>{chave}:</strong> {valor}</li>"

doc_html = html_conteudo + "<ul>" + lista + "</ul>"

with open("tabela_goiania.html", "w", encoding="utf-8") as arquivo_html:
    arquivo_html.write(doc_html)
