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
#driver.get("http://10.105.24.206/courses/course-v1:IITBombayX+TC_101+2019-20/course/")
driver.get("http://10.105.24.206/courses/course-v1:IITBombayX+TC_103+2019-20/about")
# driver.get("http://10.129.28.94")
# driver.find_element_by_xpath("//div[contains(@class, 'sign-in-btn btn')]").click()
#res1 = driver.find_element_by_xpath('//span[@id="expand-collapse-outline-all-span"]')
#res2 = driver.find_element_by_xpath('//span[@id="expand-collapse-outline-all-span"]')
#res = driver.find_element_by_xpath('//div[@class="main-cta"]')
if check_exists_by_xpath('//span[@id="expand-collapse-outline-all-span"]'):
    print("Course is Public")
elif check_exists_by_xpath('//div[@class="main-cta"]'):
    print("Not Public") 
#time.sleep(10)

driver.close()