import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Please select at least one character type."

    password = "".join(random.choice(characters) for _ in range(length))
    return password

# GUI function
def generate_password_gui():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    result_label.config(text=f"Generated Password: {password}")

# Create tkinter window
root = tk.Tk()
root.title("Password Generator")

# Length input
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)
length_label.pack()
length_entry.pack()

# Character type checkboxes
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

letters_check = tk.Checkbutton(root, text="Include letters", variable=letters_var)
numbers_check = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
symbols_check = tk.Checkbutton(root, text="Include symbols", variable=symbols_var)

letters_check.pack()
numbers_check.pack()
symbols_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

# Display result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
