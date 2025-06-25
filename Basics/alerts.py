# alerts from selenium 

from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Hadle JS Alert
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
time.sleep(2)

# Return to the current Content
#driver.switch_to.default_content 

# Handle JS Confirm
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert2 = driver.switch_to.alert
print("Next alert message:", alert2.text)
time.sleep(2)
alert2.accept()

# Handle JS Prompt
driver.find_element(By.XPATH, "//button[text() = 'Click for JS Prompt']").click()
alert3 = driver._switch_to.alert
print("Alert3:-", alert3.text)
alert3.send_keys("this is the test case!")
time.sleep(3)
alert3.accept()


time.sleep(3)
driver.quit()

