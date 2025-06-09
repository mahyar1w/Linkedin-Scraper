from database import JobDatabase
from datacollector import LinkedInJobScraper
import sqlite3
import customtkinter as ctk
from tkinter import messagebox

scraper = LinkedInJobScraper("ma1285moh@gmail.com", "mahyar12")

class CustomApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Linkedin Scraper")
        self.geometry("600x400")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.title_entry = ctk.CTkEntry(self, width=300, height=40, placeholder_text="Enter Job Title")
        self.title_entry.pack(pady=5)

        self.number_entry = ctk.CTkEntry(self, width=300, height=40, placeholder_text="Enter number of sought positions")
        self.number_entry.pack()

        self.loc_entry = ctk.CTkEntry(self, width=300, height=40, placeholder_text="Enter the Location")
        self.loc_entry.pack(pady=5)

        ctk.CTkButton(self, width=56, text="Search", command=self.search_button).place(x=225, y=145)
        self.result_button = ctk.CTkButton(self, width=56, text="Results", command=self.result)

    def search_button(self):
        num_jobs = self.number_entry.get()

        if not num_jobs.isdigit() or int(num_jobs) <= 0:
            messagebox.showerror("Invalid input", "Please enter a positive integer for the number of positions.")
            return
        else:
            scraper.init()
            scraper.login()
            scraper.search_jobs(self.title_entry.get(), self.loc_entry.get(), int(num_jobs))
            jobs = scraper.scrape_jobs()
            db = JobDatabase("jobs2.db")
            scraper.close_driver()
            db.insert_jobs(jobs)

        self.result_button.place(x=325, y=145)

    def result(self):
        new_window = ctk.CTkToplevel(self)
        new_window.title("Job Results")
        new_window.geometry("1280x720")

        table_frame = ctk.CTkScrollableFrame(new_window)
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        try:
            conn = sqlite3.connect("jobs2.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM jobs")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            for col_idx, col_name in enumerate(columns):
                header = ctk.CTkLabel(table_frame, text=col_name, font=("Arial", 12, "bold"))
                header.grid(row=0, column=col_idx, padx=5, pady=5)

            for row_idx, row in enumerate(rows):
                for col_idx, cell in enumerate(row):
                    cell_label = ctk.CTkLabel(table_frame, text=str(cell), font=("Arial", 10))
                    cell_label.grid(row=row_idx + 1, column=col_idx, padx=5, pady=5)

            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

app = CustomApp()
app.mainloop()
