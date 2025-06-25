from selenium import webdriver 

driver = webdriver.Chrome()
driver.get("https://motordna.io/")
print("Title:", driver.title)
driver.quit()