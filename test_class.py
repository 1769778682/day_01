# 1.导包
import time
from selenium import webdriver

# 2.打开浏览器
driver = webdriver.Chrome()
# 3.打开待测网址
driver.get("file:///C:/Users/sandysong"
           "/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 业务操作
driver.find_element_by_class_name("telA").send_keys("18203228558")
driver.find_element_by_class_name("dzyxA").send_keys("123@qq.com")

# 3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()