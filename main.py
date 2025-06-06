from database import JobDatabase
from  datacollector import LinkedInJobScraper

scraper = LinkedInJobScraper("ma1285moh@gmail.com", "mahyar12")
scraper.login()
scraper.search_jobs("data scientist", "united states", 20)
jobs = scraper.scrape_jobs()
db = JobDatabase("jobs2.db")
scraper.close_driver()
db.insert_jobs(jobs)