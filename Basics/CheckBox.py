# Here we learn hoe to handle the Checkbox & Radio Button and select them

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://the-internet.herokuapp.com/checkboxes"

driver = webdriver.Chrome()
driver.get(URL)

checkboxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox']")

# Loop to iterate it over all the checkboxes

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

print("All Checkbox is selected")

time.sleep(5)
driver.quit()