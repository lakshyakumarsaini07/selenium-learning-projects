from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time
try:
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID,'user-name').send_keys("standard_user")
    driver.find_element(By.ID,'password').send_keys("secret_sauce")
    driver.find_element(By.ID, 'login-button').click()
    print("Login to the server")
    time.sleep(5)
    driver.quit()

except Exception as e:
    print(e)