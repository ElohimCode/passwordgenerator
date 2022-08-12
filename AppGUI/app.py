import tkinter as tk
import pyperclip
from PIL import Image, ImageTk
from Controllers.utils import Tools


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Password Manager")
        self.config(padx=50, pady=50)

        self.canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
        self.image = Image.open("resource/logo.jpg")
        self.password_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(100, 100, image=self.password_image)
        self.canvas.grid(row=0, column=1)

        self.web_label = tk.Label(text="Website:")
        self.web_label.grid(row=1, column=0)

        self.web_entry = tk.Entry(width=35)
        self.web_entry.grid(row=1, column=1)
        self.web_entry.focus()

        self.email_user_label = tk.Label(text="Email/Username:")
        self.email_user_label.grid(row=2, column=0)

        self.email_user_entry = tk.Entry(width=56)
        self.email_user_entry.grid(row=2, column=1, columnspan=2)
        self.email_user_entry.insert(0, "bdamilola@gmail.com")

        self.password_label = tk.Label(text="Password:")
        self.password_label.grid(row=3, column=0)

        self.password_entry = tk.Entry(width=35)
        self.password_entry.grid(row=3, column=1)

        self.gen_button = tk.Button(text="Generate Password", command=self.generate_password, width=16)
        self.gen_button.grid(row=3, column=2)

        self.add_button = tk.Button(text="Add", width=47, command=self.save)
        self.add_button.grid(row=4, column=1, columnspan=2)

        self.search_button = tk.Button(text="Search", width=16, command=self.search)
        self.search_button.grid(row=1, column=2)

    def generate_password(self):
        if len(self.password_entry.get()) == 0:
            password = Tools.generate_password()
            self.password_entry.insert(0, password)
            print(f"Password generated for {self.email_user_entry.get()}...\n")
            pyperclip.copy(password)
        else:
            self.password_entry.delete(0, tk.END)
            self.generate_password()

    def save(self):
        website = self.web_entry.get()
        email = self.email_user_entry.get()
        password = self.password_entry.get()
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        Tools.save_details(website, email, password, new_data)
        print(f"Data saved successfully...\n")
        self.web_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def search(self):
        website = self.web_entry.get()
        Tools.search_info(website)
        print(f"Result for {website} is available...\n")
