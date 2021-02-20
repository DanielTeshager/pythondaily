#!/usr/bin/env python3
"""
This script opens CNN and prints the latest news headlines. 

"""
import requests
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#Chrome webdriver is located under downloads folder
driver = webdriver.Chrome(executable_path=r"/Users/danielteshager/Downloads/chromedriver")
#driver.get("http://www.python.org")

#open chrome and browes cnn.com website
driver.get("http://afalagi.com")

#prints the html title of the website
#print(driver.title)

#The dirve waits for 3 seconds after the page is fully loaded
driver.implicitly_wait(3)

#find all h3 tag elements
elem = driver.find_elements_by_xpath("//b")
#elem1 = driver.find_elements_by_xpath("//ol")
#elem = driver.find_element_by_class_name('cd__headline-text')
#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#elem = driver.find_element_by_tag_name("h1")

#go through all h3 elements and print the html innerText if it has innerText

# for el in elem:
#     text = el.text
#     print(text) if text else None

# for el in elem1:
#     text = el.text
#     print(text) if text else None 


#assert "Python" in driver.title

searchbar = driver.find_element_by_name("search")
searchbar.clear()
searchbar.send_keys("addis ababa")
searchbar.send_keys(Keys.RETURN)
mylinks = []
bahirdar_add_dict = {}
delay = 30 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
    a = driver.find_elements_by_xpath("//a")
    mylist = list(filter(lambda x:'render' in x.get_attribute('href'), a))
   
    for link in mylist:
        #print(link.get_attribute('href'))
        #link.click()
        # driver.implicitly_wait(3)
        # name = driver.find_element_by_css_selector('div.center b')
        # body = driver.find_element_by_tag_name('ol')
        # #name = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.center b'))) 
        # print(name.text)
        # print(body.text)
        try:
            session = HTMLSession()
            response = session.get(link.get_attribute('href'))
            bahirdar_add_dict[response.html.find('div.center b',first=True).text] = response.html.find('ol',first=True).text
        except requests.exceptions.RequestException as e:
            print(e)
      

        print(bahirdar_add_dict)

finally:
    #print("Loading took too much time")
    pass

#Ensures that the page loaded doesn't have no result found in the body content
assert "No results found." not in driver.page_source

#end the
driver.close()