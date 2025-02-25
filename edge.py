import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

url = "https://www.mindrisers.com.np/-"
driver.get(url)
time.sleep(5)
driver.quit()