from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list )
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "password": password,
            "email": email,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent = 4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="warning", message="no file exists.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="history", message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showwarning(title="Error", message=f"no details related to {website} is available")


# ---------------------------- UI SETUP ------------------------------#
window = Tk()
window.title("Password Manager")
image_mylock = PhotoImage(file = "logo.png")
window.config(padx = 40,pady= 40)

canvas = Canvas(width = 200,height = 200)
canvas.create_image(100,100,image= image_mylock)
canvas.grid(column = 1,row = 0)

website_label = Label(text = "Website:")
website_label.grid(column = 0,row = 1)

website_entry = Entry(width = 21)
website_entry.grid(column = 1,row = 1)
website_entry.get()
website_entry.focus()

email_entry = Entry(width = 35)
email_entry.grid(column = 1,row = 2,columnspan=2)
email_entry.insert(0,"hardik@email.com")
email_entry.get()

password_entry = Entry(width = 21)
password_entry.grid(column = 1,row = 3)
password_entry.get()

add_button = Button(text="Add",width= 36,command = save)
add_button.grid(column = 1,row = 4,columnspan = 2)

gen_password = Button(text="Generate Password",command = password_generator)
gen_password.grid(column = 2 ,row = 3)

search_button = Button(text="Search",command = find_password)
search_button.grid(column = 2,row =1 )

email_label = Label(text = "Email/Username:")
email_label.grid(column = 0,row = 2)

password_label = Label(text = "Password:")
password_label.grid(column = 0,row = 3)

window.mainloop()

