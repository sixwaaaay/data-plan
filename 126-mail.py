# 网易邮件发送
# 网易邮箱元素id和class是动态生成的
#
# 使用CSS选择器模糊匹配
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.126.com/")

driver.implicitly_wait(30)

# login
frame = driver.find_element(By.CSS_SELECTOR, 'iframe[id^="x-URS-iframe"')
driver.switch_to.frame(frame)
driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(os.getenv('username'))
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(os.getenv('password'))
driver.find_element(By.CSS_SELECTOR, '#dologin').click()
driver.switch_to.default_content()

# to edit mail
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR, '.ga0').click()

# edit
driver.find_element(By.CSS_SELECTOR, 'div[id^="_mail_emailin"] > input').send_keys(os.getenv("target"))  # 目标用户
driver.find_element(By.CSS_SELECTOR, 'input[id$="subjectInput"]').send_keys("主题")  # 邮件标题

# content
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".APP-editor-iframe"))
driver.find_element(By.CSS_SELECTOR, '.nui-scroll[spellcheck="false"]').send_keys("content")  # 邮件内容
driver.switch_to.default_content()

# send
driver.find_element(By.CSS_SELECTOR, '.nui-ico-sent-white').click()
