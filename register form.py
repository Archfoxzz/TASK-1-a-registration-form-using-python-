#importing libraries 

import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    # Here you can add code to save the data or process it as needed
   
    if name and email and password:
        messagebox.showinfo("Registration Successful", f"Welcome, {name}!")
        # Clear the form fields after submission
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Register", command=submit_form)
submit_button.pack(pady=20)

# Run the application
root.mainloop()