# 导包
import time

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost/Home/user/login.html")
# 输入手机号
# driver.find_element_by_name("username").send_keys(Keys.CONTROL, 'a')
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("13812345346")
# 输入密码
driver.find_element_by_name("password").send_keys("123456")
# 输入验证码
driver.find_element_by_name("verify_code").send_keys("8888")
# 点击登录
driver.find_element_by_name("sbtbutton").click()
# 暂停3秒
time.sleep(3)
# 关闭浏览器
# driver.quit()

