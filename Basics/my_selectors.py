from selenium import webdriver 
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.get("https://example.com")


elem1 = driver.find_element(By.XPATH, "//h1")
elem2 = driver.find_element(By.CSS_SELECTOR, 'p')


print('Heading:', elem1.text)
print('Paragraph:', elem2.text)
driver.quit()