from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


driver.get("http://the-internet.herokuapp.com/login")

search_username = ("tomsmith")
search_password = ("SuperSecretPassword!")

input_login = ('//*[@id="username"]')
input_password = ('//*[@id="password"]')

button_login = ('/html/body/div[2]/div/div/form/button')
green_plashka = ('You logged into a secure area!')

search_input_login = driver.find_element(By.XPATH,input_login)
search_input_login.send_keys(search_username)
sleep(2)

search_input_password = driver.find_element(By.XPATH,input_password)
search_input_password.send_keys(search_password)
sleep(2)

search_input_button = driver.find_element(By.XPATH,button_login)
search_input_button.send_keys(Keys.ENTER)
sleep(2)

print(green_plashka)

driver.quit()