from AppGUI.app import App

print(f"""Password Application Shell
Copyright (C) Earnstein Tech. All right reserved.

Application is running...

- Enter website, username or email
- Click on generate to get a length of password
- Click on save to store the data in database
- Search with website keyword to recall the data

""")

if __name__ == '__main__':
    app = App()
    app.mainloop()
