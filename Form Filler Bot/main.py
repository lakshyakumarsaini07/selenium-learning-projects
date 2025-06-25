"""
Form Filler Bot (Job Application or Survey Automation)


Task: Fill out a multi-page form (e.g., Google Form or sample form site) using Selenium.

Concepts Used:
Input fields
Radio buttons / checkboxes
Dropdowns
Button clicking
Navigation

Bonus: Handle validation messages and screenshots of each page."""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


URL = "https://www.techlistic.com/p/selenium-practice-form.html"

driver = webdriver.Chrome()
driver.get(URL)

# Find & trigeer FIRSTNAME, LASTNAME
driver.find_element(By.XPATH, "//input[@name = 'firstname']").send_keys("Lakshya")
driver.find_element(By.XPATH, "//input[@name = 'lastname']").send_keys("saini")

# GENDER - BY DEFAULT MALE 
driver.find_element(By.ID, "sex-0").click()

# Select the year of experience 
driver.find_element(By.XPATH, "//input[@id = 'exp-0']").click()

# Select data 
driver.find_element(By.ID, "datepicker").send_keys("2025-06-25")

# Select Skills
driver.find_element(By.CLASS_NAME, "control-group")

# Select the continent
conti_dropdown = Select(driver.find_element(By.ID, "continents"))
conti_dropdown.select_by_visible_text("Asia")

#Uplaod the file 
file_path = 'L:\selenium\Form Filler Bot\ChatGPT Image Jun 23, 2025, 11_40_33 AM.png'
driver.find_element(By.ID, "photo").send_keys(file_path)

#Submit 
driver.find_element(By.ID, "submit").click()
time.sleep(5)

print(" Filled Details Successfully!!")

driver.quit()



