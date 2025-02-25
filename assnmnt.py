from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.ui import Select
from selenium. webdriver. common.alert import Alert

#set up a driver installation
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#provide a website
url = "https://merolagani.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

Market = driver.find_element(By.XPATH, "//a[normalize-space()='Market']")
Market.click()
time.sleep(2)
try:
    alert = Alert(driver)
    alert.dismiss()
except:
    print("no Alert found")
Live_trading = driver.find_element(By.XPATH, "//a[normalize-space()='Live Trading']")
Live_trading.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,400);")
time.sleep(2)
# Click on company 
ACLBSL = driver.find_element(By.XPATH, "//a[normalize-space()='ACLBSL']")
ACLBSL.click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
# Scroll down to load more content
driver.execute_script("window.scrollBy(0,400);")
time.sleep(2)

price_history = driver.find_element(By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab']")
price_history.click()
time.sleep(2)

date = driver.find_element(By.XPATH, "//input[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter']")
date.send_keys("02/02/2025")
time.sleep(2)
search = driver.find_element(By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lbtnSearchPriceHistory']")
search.click()
time.sleep(2)

driver.quit()