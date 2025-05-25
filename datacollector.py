from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)


EMAIL = "ma1285moh@gmail.com"
PASSWORD = "mahyar12"


try:
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

finally:
    driver.quit()