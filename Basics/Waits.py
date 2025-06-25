from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

URL = "https://www.saucedemo.com/"

driver = webdriver.Chrome()
driver.get(URL)

wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
username.send_keys("standard_user")

password = wait.until(EC.presence_of_element_located((By.ID,'password')))
password.send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()


print("Username & Password is found and filled, Login Succesfully")


time.sleep(5)
driver.quit()
