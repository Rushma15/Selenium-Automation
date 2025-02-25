from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set up a driver installation
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#provide a website
url = "https://filebin.net/"

driver.get(url)
driver.maximize_window()
time.sleep(5)

select_file = driver.find_element(*(By.XPATH,"//input[@id='fileField']"))
select_file.send_keys("C:/Users/Rush/Desktop/images.jpg")
# select_file.click()
time.sleep(5)

more = driver.find_element(By.XPATH,("//a[@id='dropdownFileMenuButton']"))
more.click()
time.sleep(4)

download =driver.find_element(By.XPATH,("//a[normalize-space()='Download file']"))
download.click()
time.sleep(4)


driver.quit()