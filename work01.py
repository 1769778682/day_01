# 作业一
# 导包
import time

from selenium import webdriver
# 打开浏览器
driver = webdriver.Chrome()
# 运行待测网址
driver.get("http://localhost/Home/user/reg.html")
# 暂停3秒
time.sleep(3)
# 输入手机号
driver.find_element_by_name("username").send_keys("13812345348")
# 输入验证码
driver.find_element_by_name("verify_code").send_keys("8888")
# 输入密码
driver.find_element_by_name("password").send_keys("123456")
# 再次确认密码
driver.find_element_by_id("password2").send_keys("123456")
# 输入推荐人手机号
driver.find_element_by_name("invite").send_keys("13812345678")
# 点击立即注册
driver.find_element_by_class_name("J_btn_agree").click()
time.sleep(3)
# 关闭浏览器
driver.quit()
