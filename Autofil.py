from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

import re #for regular expression
import random
import string

#set up a driver installation
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#provide a website
url = "https://www.mindrisers.com.np/contact-us"

driver.get(url)
driver.maximize_window()
time.sleep(5)

driver.execute_script("window.scrollBy(0,600);")
time.sleep(5)

#findlocators
name_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))

def is_valid_email(email):
    try:
        email_pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.search(email_pattern,email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    
    #generation of random input values
def generate_random_email():
    domain = "automate.com"
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email = random_string +"@" + domain
    return email
def generate_random_name():
    return''.join(random.choices(string.ascii_letters,k=8))
    
def generate_random_phone():
    # return "+977-98" + ''.join(random.choices(string.digits,k=8))
    return "+977-98" + ''.join(random.choices(string.digits,k=8))

#generate random name
name = generate_random_name()
email = generate_random_email()
phone = generate_random_phone()

# email_field.clear_field()

if not name:
    print("field can not be empty")

name_field.clear()
name_field.send_keys(name)
time.sleep(3)

if is_valid_email(email):
    print(" email valid")
else:
    print("invalid email")
    
email_field.clear()
email_field.send_keys(email)
time.sleep(2)

phone_field.clear()
phone_field.send_keys(phone)
time.sleep(2)



# time.sleep(5)
driver.quit()