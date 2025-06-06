from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

if os.name == "posix":
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
elif os.name == "nt":
    driver = webdriver.Chrome()



class LinkedInJobScraper:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def login(self):
        driver.get('https://www.linkedin.com/login')
        time.sleep(2)
        
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(self.username)

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(self.password)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

    def search_jobs(self, job_title, country, num_jobs):
        self.num_jobs = num_jobs
        driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')
        time.sleep(5)

        job_search_bar = driver.find_element(By.CSS_SELECTOR, """input[aria-label="Search by title, skill, or company"]""")
        job_search_bar.send_keys(job_title)

        country_search_bar = driver.find_element(By.CSS_SELECTOR, "input[aria-label='City, state, or zip code']")
        country_search_bar.send_keys(Keys.CONTROL + "a")
        country_search_bar.send_keys(Keys.DELETE)
        country_search_bar.send_keys(country + Keys.ENTER)
        time.sleep(4)

        jobs_window = driver.find_element(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list > div")
        scrolled_jobs = 0
        while scrolled_jobs < num_jobs:
            driver.execute_script("arguments[0].scrollBy(0, 500);", jobs_window)
            scrolled_jobs += 1
            time.sleep(0.6)

    def scrape_jobs(self):
        jobs = driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__title")
        companies = driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__subtitle")
        locations = driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__caption")
        links = driver.find_elements(By.CLASS_NAME, "job-card-container__link")

        job_data = []
        for job, company, location, link in zip(jobs, companies, locations, links):
            if len(job_data) < self.num_jobs:
                job_data.append({
                    "title": job.text,
                    "company": company.text,
                    "location": location.text,
                    "link": link.get_attribute("href")
                })
            else:
                break

        return job_data

    def close_driver(self):
        driver.quit()
