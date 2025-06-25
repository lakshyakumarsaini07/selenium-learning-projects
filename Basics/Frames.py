#Here we learn how to hadle 'iframes'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 



URL = "https://the-internet.herokuapp.com/iframe"

driver = webdriver.Chrome()
driver.get(URL)

driver.switch_to.frame("mce_0_ifr")
editor = driver.find_element(By.ID, "tinymce")
editor.clear()
editor.send_keys("Hello from inside the frame!")

driver.switch_to.default_content()
print("Frame interaction done")

time.sleep(4)
driver.quit()