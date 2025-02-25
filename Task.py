from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set up a driver installation
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#provide a website
url = "https://merolagani.com/"

driver.get(url)
driver.maximize_window()
time.sleep(5)

select_file = driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
select_file.click()
time.sleep(2)

select_file = driver.findElement(By.xpath("//a[normalize-space()='Live Trading']"))
select_file.click()

time.sleep(5)

driver.quit()