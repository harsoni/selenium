from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\usre\django_projects\selenium\drivers\chromedriver.exe")
driver.get("http://google.com")
driver.maximize_window()
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("India WC 2019 news")
inputElement.submit()

result = driver.find_elements_by_xpath('//h3[@class="LC20lb"]')

for i in range(len(result)):
    print(result[i].text)
time.sleep(10)
driver.close()