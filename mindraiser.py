from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://www.mindrisers.com.np/online-admission#admission-form"


driver.get(url)
driver.maximize_window()
time.sleep(2)

full_name = driver.find_element(By.XPATH,("//input[@id='full_name']"))
email =driver.find_element(By.XPATH,("//input[@id='email']"))
mobile_no = driver.find_element(By.XPATH,("//input[@id='mobile_no']"))
collage = driver.find_element(By.XPATH,("//input[@id='college']"))

full_name.send_keys("Rushma Karki")
time.sleep(2)
email.send_keys("karkirushu@gmail.com")
time.sleep(2)
mobile_no.send_keys("123456789")
time.sleep(2)
collage.send_keys("Tribhuvan University")

time.sleep(5)
driver.quit()