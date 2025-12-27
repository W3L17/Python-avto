from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


chrome_options = Options()
chrome_options.add_argument("--incognito")  # Режим без кэша
chrome_options.add_argument("--disable-cache")

#Упражнение 1. Клик по кнопке с CSS-классом

driver.get("http://uitestingplayground.com/classattr")

search_locator = ('//button[contains(@class, "btn-primary") and contains(@class, "btn-test")]')
search_input = driver.find_element(By.XPATH,search_locator)
search_input.send_keys(Keys.ENTER) 

sleep(10)