from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '&', '*']
    nr_letters = random.randint(4,6)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    new_password = "".join(password_list)
    password.delete(0,END)
    password.insert(END,f"{new_password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def Add():
    add_website = website.get()
    add_username = username.get()
    add_password = password.get()
    new_data = {
        add_website: {
            "email": add_username,
            "password": add_password,
        }
    }

    if add_website == "" or add_username == "" or add_password == "":
        messagebox.showinfo(title="Error", message="Make sure you haven't let any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"These are the details entered:\nWebsite: {add_website}\nEmail/Username: {add_username}\nPassword: {add_password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    #Reading old data
                    data = json.load(file)
                    #Updating old data with new data
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    #Saving updated data
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                password.delete(0, END)
                website.delete(0, END)

# ---------------------------- Search password------------------------------- #
def search_password():
    add_website = website.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if add_website in data:
                found = data[add_website]["password"]
                email = data[add_website]["email"]
                password.insert(END, f"{found}")
                username.delete(0,END)
                username.insert(END, f"{add_website}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {add_website} exists.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height= 200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

website = Entry(width=21)
website.grid(row=1, column=1, columnspan=1)

username_text = Label(text="Email/Username:")
username_text.grid(row=2, column=0)

username = Entry(width=35)
username.grid(row=2, column=1, columnspan=2)
username.focus()
username.insert(END, "moscaliuctimotei@gmail.com")

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password = Entry(width=21)
password.grid(row=3, column=1, columnspan=1)

password_button = Button(text="Generate Password", width=15, command=password_generator)
password_button.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=36, command=Add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column= 2)



window.mainloop()