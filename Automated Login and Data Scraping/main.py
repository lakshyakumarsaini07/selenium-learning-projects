"""
Automated Login and Data Scraping
Task: Automate login to a website (like https://quotes.toscrape.com/login) and scrape all quotes after login then Store the data in a CSV file.

Concepts Used:
Form filling
XPath/CSS selectors
Click actions
Pagination
Text extraction

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd 


URL = "https://quotes.toscrape.com/login"

driver = webdriver.Chrome()
driver.get(URL)

driver.find_element(By.ID, "username").send_keys("User123")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

print("Login successful.\nScraping quotes...")


quotes_data = []

while True:
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME,"text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME,"tag")]

        quotes_data.append({
            'Quote' : text,
            'Author' : author,
            'Tags' : ", ".join(tags)
        })

    try : 
        next_btn = driver.find_element(By.XPATH, '//li[@class = "next"]/a')
        next_btn.click()
        time.sleep(2)
    except:
        print("No more pages")
        break

df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index= False)

print("Data Scraping Complete!!!")

time.sleep(3)
driver.quit()
