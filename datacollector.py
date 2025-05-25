from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/login")

time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys("ma1285moh@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("mahyar12")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

try:
    search_box = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    search_box.click()
except:
    driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/button').click()
    search_box = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    search_box.click()
    
search_box.send_keys("Python Developer")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

profiles = driver.find_elements(By.XPATH, "//span[@dir='ltr']/span[@aria-hidden='true']")
for profile in profiles:
    print(profile.text)

driver.quit()