#Agi - Pesquisar - Cenário 4 - Validação do Botão "Pesquisar". 

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.maximize_window()

#Acessa o Site  
driver.get("https://blogdoagi.com.br/")   
time.sleep(2)
                                  
#Clica no botão da Lupa
click_button = driver.find_element(By.ID, "search-open").click() 
time.sleep(1)  

#Imprimir a informação "1 - Lupa" no terminal, indicando que foi clicada.
btn_txt = driver.find_element(By.ID, "search-open").text
print(("1 - Lupa"), btn_txt)


#Preencher o campo de pesquisa
search_box = driver.find_element(By.CSS_SELECTOR, ".desktop-search .search-field").send_keys("Agibank cresce 5x")

#Imprimir a informação "2 - Campo Pesquisar" no terminal indicando que foi clicado no campo e inserido uma sentença para a pesquisa.
btn_txt = driver.find_element(By.CSS_SELECTOR, ".desktop-search .search-field").text
print(("2 - Campo Pesquisar"), btn_txt)


#Clicar no botão Pesquisar
click_button = driver.find_element(By.XPATH, "//input[@value='Pesquisar']").click() 

#Imprimir a informação "3 - Clicando no Botão Pesquisar " no terminal indicando que foi clicado no botão "Pesquisar".
btn_txt = driver.find_element(By.XPATH, "//input[@value='Pesquisar']").text
print(("3 - Clicando no Botão Pesquisar"), btn_txt)


#Imprime a informação "4 - É encontrado o artigo da pesquisa, após clicar no botão Pesquisar:" + o "Titulo da Pesquisa escolhida" no terminal.     
link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "uso da Inteligência Artificial").text
print(("4 - É encontrado o artigo da pesquisa, após clicar no botão Pesquisar:"),link_text)

# close browser window
driver.quit()
