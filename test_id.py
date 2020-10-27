import time

from selenium import webdriver

# driver = webdriver.Chrome()
fir = webdriver.Firefox()

fir.get("file:///C:/Users/sandysong"
        "/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
element = fir.find_element_by_id('userA').send_keys('admin')
print("开始时间", time.time())
fir.find_element_by_id('passwordA').send_keys('123456')
print("结束时间",time.time())

time.sleep(3)
# driver.quit()
fir.quit()

