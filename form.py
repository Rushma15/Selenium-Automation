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

firstname = driver.find_element(By.XPATH,"//input[@id='first-name']")
Lastname = driver.find_element(By.XPATH,"//input[@id='last-name']")
Job_title = driver.find_element(By.XPATH,"//input[@id='job-title']")
Education_level = driver.find_element(By.XPATH,"//input[@id='radio-button-2']")
Gender1 = driver.find_element(By.XPATH,"//input[@id='checkbox-1']")
Gender2 = driver.find_element(By.XPATH,"//input[@id='checkbox-2']")

year_dropdown=driver.find_element(By.XPATH,"//select[@id='select-menu']")


firstname.send_keys("john")
time.sleep(2)
Lastname.send_keys("Doe")
time.sleep(2)
Job_title.send_keys("QA Engineer")
time.sleep(2)
Education_level.click()
time.sleep(2)
Gender1.click()
time.sleep(2)
Gender2.click()
time.sleep(2)


# scrolling down the page
driver.execute_script("window.scrollBy(0.200);")
time.sleep(2)


time.sleep(5)
driver.quit()