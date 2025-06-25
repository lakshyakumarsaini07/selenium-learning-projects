#Here we Learn How to take an ScreenShot of an page 

from selenium import webdriver

URL = "https://example.com"

driver = webdriver.Chrome()
driver.get(URL)

driver.save_screenshot("ScreenShot.png")

print("Screenshot saved!")
driver.quit()