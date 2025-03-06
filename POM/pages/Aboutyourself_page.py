from selenium.webdriver.common.by import By

class AboutYourselfPage:
    def __init__(self, driver):
        self.driver = driver
        self.full_name_textbox = (By.XPATH,"//input[@id='fullname']")
        self.phone_textbox = (By.XPATH,"//input[@id='phone']")
        self.email_text = (By.XPATH,"//input[@id='email']")
        self.hobby_textbox = (By.XPATH,"//input[@id='hobby']")  
    

    def open_page(self, url):
        self.driver.get(url)

    def enter_full_name(self, full_name):
        self.driver.find_element(*self.full_name_textbox).send_keys(full_name)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)

    def enter_email(self, email):
        self.driver.find_element(*self.email_text).send_keys(email)

    def enter_hobby(self,hobby):
        self.driver.find_element(*self.hobby_textbox).send_keys(hobby)
        