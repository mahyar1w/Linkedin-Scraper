from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


class LinkedInJobScraper:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def init(self):
        if os.name == "posix":
            service = Service(executable_path='/usr/bin/chromedriver')
            self.driver = webdriver.Chrome(service=service)
        elif os.name == "nt":
           self.driver = webdriver.Chrome()
   


    def login(self):
        
        self.driver.get('https://www.linkedin.com/login')
        time.sleep(2)
        
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys(self.username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(self.password)

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

    def search_jobs(self, job_title, country, num_jobs):
        self.num_jobs = num_jobs
        self.driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')
        time.sleep(5)

        job_search_bar = self.driver.find_element(By.CSS_SELECTOR, """input[aria-label="Search by title, skill, or company"]""")
        job_search_bar.send_keys(job_title)

        country_search_bar = self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='City, state, or zip code']")
        country_search_bar.send_keys(Keys.CONTROL + "a")
        country_search_bar.send_keys(Keys.DELETE)
        country_search_bar.send_keys(country + Keys.ENTER)
        time.sleep(4)

        self.jobs_window = self.driver.find_element(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list > div")
    def scrape_jobs(self):
        job_data = []
        scraped_job_links = set()
        while len(job_data) < self.num_jobs:
            for _ in range(25):
                self.driver.execute_script("arguments[0].scrollBy(0, 500);", self.jobs_window)
                time.sleep(0.6)

            jobs = self.driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__title")
            companies = self.driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__subtitle")
            locations = self.driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__caption")
            links = self.driver.find_elements(By.CLASS_NAME, "job-card-container__link")

            
            for job, company, location, link in zip(jobs, companies, locations, links):
                scraped_job_link = link.get_attribute("href")
                if len(job_data) < self.num_jobs :
                    if scraped_job_link not in scraped_job_links:
                        job_data.append({
                            "title": job.text,
                            "company": company.text,
                            "location": location.text,
                            "link": scraped_job_link
                    })
                    scraped_job_links.add(scraped_job_link)
                else:
                    break

            try:
                self.driver.find_element(By.CSS_SELECTOR,"""button[aria-label="View next page"]""").click()
                time.sleep(3)
            except:
                print("no more pages.")
                break

        return job_data

    def close_driver(self):
        self.driver.quit()