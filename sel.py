# Import necessary driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


# setup a driver installation
# driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# provide a website
url="https://www.mindrisers.com.np/-"
driver.get(url)
# driver.maximize_window()
time.sleep(5)

driver.quit()