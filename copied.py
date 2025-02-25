from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.alert import Alert

# Set up a driver installation
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Provide a website
url = "https://merolagani.com/"
driver.get(url)
driver.maximize_window()

# Wait for 'Market' link to be clickable and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Market']"))).click()

# Handle alert if present
try:
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())  # Wait for alert to appear
    alert.dismiss()
except:
    print("No Alert found")

# Wait for 'Live Trading' link to be clickable and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Live Trading']"))).click()

# Scroll down to load more content
driver.execute_script("window.scrollBy(0,400);")
time.sleep(2)

# Click on the company 'ACLBSL'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='ACLBSL']"))).click()

# Switch to the new tab opened after clicking the company link
time.sleep(2)  # Ensure the new tab has opened before switching
driver.switch_to.window(driver.window_handles[1])

# Scroll down to load more content
driver.execute_script("window.scrollBy(0,400);")
time.sleep(2)

# Click on 'Price History' tab
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab']"))).click()

# Wait for price history to load
time.sleep(5)

# Enter date in the price history input field
date = driver.find_element(By.XPATH, "//input[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter']")
date.send_keys("02/02/2025")

# Click on 'Search' button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lbtnSearchPriceHistory']"))).click()

# Wait for results to load
time.sleep(3)

# Close the browser
driver.quit()
