from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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