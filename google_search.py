from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\usre\django_projects\selenium\drivers\chromedriver.exe")
driver.get("http://google.com")
driver.maximize_window()
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("WC 2019")
inputElement.submit()
time.sleep(5)

driver.close()