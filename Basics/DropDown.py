# Here we learn How to Handle the Dropdown List


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select


URL= "https://the-internet.herokuapp.com/dropdown"

driver = webdriver.Chrome()
driver.get(URL)

dropdown = Select(driver.find_element(By.ID, 'dropdown'))
dropdown.select_by_visible_text("Option 2")

print("Selected the dropdown option")

driver.quit()



