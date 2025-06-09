import sqlite3
import os
class JobDatabase:
    def __init__(self, db_name="jobs.db"):
        self.db_name = db_name
        
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                location TEXT,
                link TEXT UNIQUE
            )
        """)
        conn.commit()
        conn.close()

    def insert_jobs(self, jobs):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        for job in jobs:
            if isinstance(job, dict):
                title = job.get("title", "")
                company = job.get("company", "")
                location = job.get("location", "")
                link = job.get("link", "")
            elif isinstance(job, (tuple, list)):
                title, company, location, link = job
            else:
                continue

            try:
                cursor.execute("""
                    INSERT INTO jobs (title, company, location, link)
                    VALUES (?, ?, ?, ?)
                """, (title, company, location, link))
            except sqlite3.IntegrityError:
                print(f"Duplicate job skipped: {title} - {company}")
                continue
        conn.commit()
        conn.close()

    def get_all_jobs(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT title, company, location, link FROM jobs")
        rows = cursor.fetchall()
        conn.close()
        return rows


