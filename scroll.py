from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://www.mindrisers.com.np/"


driver.get(url)
driver.maximize_window()

# calculate height of page
page_height = driver.execute_script("return document.body.scrollHeight")

scroll_speed = 1000
scroll_iteration = int(page_height/scroll_speed)

# loop to perform scroll
for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(2)


title = driver.title
print(title)

time.sleep(2)
driver.quit()