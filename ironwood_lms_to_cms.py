from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Chrome(r"C:\Users\usre\django_projects\selenium\drivers\chromedriver.exe")
driver.get("http://10.105.24.206/login?next=%2F")

email = driver.find_element_by_name("email")
email.send_keys("harsh@gmail.com")
passw = driver.find_element_by_name("password")
passw.send_keys("admin123")
driver.find_element_by_xpath('//button[contains(text(), "Sign in")]').click()

#driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("http://10.105.24.206:18010")

if check_exists_by_xpath('//span[@class="account-username"]'):
    print("You are here")
else:
    print("First login to lms")
time.sleep(5)
driver.close()

driver.switch_to.window(driver.window_handles[0])
driver.close()
