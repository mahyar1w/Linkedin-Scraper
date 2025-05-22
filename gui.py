import customtkinter as ctk
from tkinter import messagebox  

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

        ctk.CTkButton(self, width=56, text="search", command=self.search_button).place(x=225, y=100)
        self.result_button = ctk.CTkButton(self, width=56, text="results", command=self.result)

    def search_button(self):
        number_text = self.number_entry.get()

        if not number_text.isdigit() or int(number_text) <= 0:
            messagebox.showerror("Invalid input", "Please enter a positive integer for the number of positions.")
            return

        self.result_button.place(x=325, y=100)

    def result(self):
        new_window = ctk.CTkToplevel(self)
        new_window.title("results")
        new_window.geometry("1280x720")
        ctk.CTkLabel(new_window, text_color="green", text="place holder", font=("Arial", 48)).pack(expand=True)

if __name__ == "__main__":
    app = CustomApp()
    app.mainloop()
