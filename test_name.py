import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///C:/Users/sandysong"
           "/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_name("userA").send_keys("admin")
driver.find_element_by_name("passwordA").send_keys("123456")
time.sleep(3)
driver.quit()
