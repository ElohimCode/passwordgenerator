import string
from tkinter import messagebox
import random
import json


class Tools:
    """Tools to generate password, save and search saved information."""
    @staticmethod
    def generate_password():
        """
        Static method that generate passwords
        :return: a length of password
        :rtype: string
        """
        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        nr_letters, nr_symbols, nr_numbers = random.randint(8, 10), random.randint(2, 4), random.randint(2, 4)

        password_letters = [random.choice(letters) for _ in range(nr_letters)]
        password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
        password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

        password_list = password_letters + password_symbols + password_numbers
        random.shuffle(password_list)
        return "".join(password_list)

    @staticmethod
    def save_details(website, email, password, new_data):
        """
        Static method that store data into a json file
        :param website: website address
        :param email: email or username
        :param password: password attributed to the email
        :param new_data: data to be stored
        :return: None
        """
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                                  f"\npassword: {password} \nIs it okay to save?")

            if is_ok:
                try:
                    with open("resource/data.json", "r") as data_file:
                        # Reading old data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("resource/data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    # Updating old data with new data
                    data.update(new_data)
                    with open("resource/data.json", "w") as data_file:
                        # saving updated data
                        json.dump(data, data_file, indent=4)

    @staticmethod
    def search_info(website):
        """
        Static method that search for data based on website
        :param website: website address
        :return: None
        """
        try:
            with open("resource/data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file Found")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\npassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exist")
