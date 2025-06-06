from database import JobDatabase
from  datacollector import LinkedInJobScraper

scraper = LinkedInJobScraper("username", "password")
scraper.login()
scraper.search_jobs("data scientist", "united states", 20)
jobs = scraper.scrape_jobs()
db = JobDatabase("jobs2.db")
scraper.close_driver()
db.insert_jobs(jobs)