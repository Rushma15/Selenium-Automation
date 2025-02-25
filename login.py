from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://formy-project.herokuapp.com/form"


driver.get(url)
driver.maximize_window()
time.sleep(2)

username = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"login-button")
username.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)

login_button.click()
title = driver.current_url
if (title =="https://www.saucedemo.com/v1/inventory.html"):
    print("login successful")
else:
    print("login unsuccessful")


# calculate height of page
# page_height = driver.execute_script("return document.body.scrollHeight")

# scroll_speed = 1000
# scroll_iteration = int(page_height/scroll_speed)

# loop to perform scroll
# for _ in range(scroll_iteration):
#     driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
#     time.sleep(2)


# title = driver.title
# print(title)

time.sleep(5)
driver.quit()

# selecting input path
# By id
# By Name
# By Xpath
# By class
#     by css
