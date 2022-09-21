# 论规范的网页有多舒服

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.bilibili.com/v/popular/history")
up_names = driver.find_elements(By.CSS_SELECTOR, ".up-name__text")
plays = driver.find_elements(By.CSS_SELECTOR, ".play-text")
likes = driver.find_elements(By.CSS_SELECTOR, ".like-text")
hints = driver.find_elements(By.CSS_SELECTOR, ".history-hint")
video_names = driver.find_elements(By.CSS_SELECTOR, ".video-name")

for up, play, like, name, hint in zip(up_names, plays, likes, video_names, hints):
    print(f"{name.text},{up.text},{like.text},{play.text},{hint.text}")
