# 1.导包
import time

from selenium import webdriver
# 2.创建浏览器驱动对象
# driver = webdriver.Chrome()
fir = webdriver.Firefox()
# 3.打开测试网址
# driver.get("https://www.baidu.com/")
fir.get("https://www.baidu.com/")
# 4.执行业务操作
time.sleep(3)
# 5.关闭浏览器
# driver.quit()
fir.quit()


