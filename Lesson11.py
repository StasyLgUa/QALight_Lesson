from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
driver.maximize_window()
url = 'https://bank.gov.ua/ua/markets/exchangerates'

currency_button_usd = driver.find_element()
#find elements
#//td[contains(text(), "USD")]/parent::tr/td[@class="value-name"]/a
#//td[contains(text(), "USD")]/parent::tr/td[5]

