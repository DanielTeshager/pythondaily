#!/usr/bin/env python3
"""
This script opens CNN and prints the latest news headlines. 

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#Chrome webdriver is located under downloads folder
driver = webdriver.Chrome(executable_path=r"/Users/danielteshager/Downloads/chromedriver")
#driver.get("http://www.python.org")

#open chrome and browes cnn.com website
driver.get("https://www.cnn.com")

#prints the html title of the website
print(driver.title)

#The dirve waits for 3 seconds after the page is fully loaded
driver.implicitly_wait(3)

#find all h3 tag elements
elem = driver.find_elements_by_xpath("//h3")
#elem = driver.find_element_by_class_name('cd__headline-text')
#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#elem = driver.find_element_by_tag_name("h1")

#go through all h3 elements and print the html innerText if it has innerText
for el in elem:
    text = el.text
    print(text) if text else None


#assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("Christmas")
# elem.send_keys(Keys.RETURN)

#Ensures that the page loaded doesn't have no result found in the body content
assert "No results found." not in driver.page_source

#end the
driver.close()