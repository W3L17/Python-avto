from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


driver.get("https://the-internet.herokuapp.com/inputs")

search_id = ('/html/body/div[2]/div/div/div/div/input')
search_input = driver.find_element(By.XPATH,search_id)
search_input.send_keys('Sky')
sleep(3)
search_input.clear()
sleep(3)
search_input.send_keys('Pro')
driver.quit()


sleep(10)