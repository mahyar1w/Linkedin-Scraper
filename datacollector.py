from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/login')
time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys("email")

password = driver.find_element(By.ID, "password")
password.send_keys("password")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(15)

driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')
time.sleep(3)

job_title="data scientist"

country = "united states"

#number_of_results = 

job_search_bar = driver.find_element(By.CSS_SELECTOR, """input[aria-label="Search by title, skill, or company"]""")
job_search_bar.send_keys(job_title)

country_search_bar = driver.find_element(By.CSS_SELECTOR, """input[aria-label="City, state, or zip code"]""")
country_search_bar.send_keys(Keys.CONTROL + "a")
country_search_bar.send_keys(Keys.DELETE)
country_search_bar.send_keys(country+Keys.ENTER)
time.sleep(4)

jobs_window = driver.find_element(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list > div")

for i in range(20):
    driver.execute_script("arguments[0].scrollBy(0, 500);", jobs_window)
    #jobs_window.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.6)


jobs = driver.find_elements(By.CLASS_NAME,"artdeco-entity-lockup__title")
for job in jobs:
    print(job.text)
companies = driver.find_elements(By.CLASS_NAME,"artdeco-entity-lockup__subtitle")
for company in companies:
    print(company.text)
locations = driver.find_elements(By.CLASS_NAME,"artdeco-entity-lockup__caption")
for location in locations:
    print(location.text)
links = driver.find_elements(By.CLASS_NAME,"job-card-container__link")
for link in links:
    print(link.get_attribute("href"))

#driver.find_element(By.CSS_SELECTOR,"""button[aria-label="View next page"]""").click()

time.sleep(3)

driver.quit()