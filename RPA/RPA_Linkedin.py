from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(r'.\choromedriver.exe')#caminho contendo o arquivo do browser

browser.get("https://www.linkedin.com/login")#Browser.get usado para abrir LINK

input_email = browser.find_element_by_id("username")
input_email.send_keys("emailquevaiserdigitado")
input_senha = browser.find_element_by_id("password")
input_senha.send_keys("senhaquevaiserdigitado")

btn_login = brower.find_element_by_xpath("//button[@type='Submit']")
btn_login.click()

buscar = browser.find_element_by_id("//input[@placeholder='Pesquisar']")
buscar.send_keys("Python")
buscar.send_keys(Keys.RETURN)#keys.return clica em "enter"

time.sleep(37
           )

filtro_vagas =  brower.find_element_by_xpath("//button[@aria-label='Vagas']")
filtro_vagas.click()



