from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "email id used to log into LinkedIn"
ACCOUNT_PASSWORD = 'password used to log into LinkedIn'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("LinkedIn link with your preferred job title and location with "easy apply" selected")

time.sleep(2)
sign_in_button = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/section/div/div/div/div[2]/button")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/section/div/div/form/div[1]/div[1]/div/div/input")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/section/div/div/form/div[1]/div[2]/div/div/input")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")
