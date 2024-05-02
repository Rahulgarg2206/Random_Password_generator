import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    def copy_to_clipboard():
        password = generated_password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

    def generate():
        length = int(password_length_entry.get())
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(0, password)

    root = tk.Tk()
    root.title("Advanced Password Generator")
    root.configure(bg="#f0f0f0")

    main_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
    main_frame.pack()

    password_length_label = tk.Label(main_frame, text="Password Length:", bg="#f0f0f0")
    password_length_label.grid(row=0, column=0, sticky="w")
    password_length_entry = tk.Entry(main_frame, width=5)
    password_length_entry.grid(row=0, column=1)

    uppercase_var = tk.BooleanVar()
    uppercase_checkbutton = tk.Checkbutton(main_frame, text="Uppercase", variable=uppercase_var, bg="#f0f0f0")
    uppercase_checkbutton.grid(row=1, column=0, sticky="w")

    lowercase_var = tk.BooleanVar()
    lowercase_checkbutton = tk.Checkbutton(main_frame, text="Lowercase", variable=lowercase_var, bg="#f0f0f0")
    lowercase_checkbutton.grid(row=2, column=0, sticky="w")

    digits_var = tk.BooleanVar()
    digits_checkbutton = tk.Checkbutton(main_frame, text="Digits", variable=digits_var, bg="#f0f0f0")
    digits_checkbutton.grid(row=3, column=0, sticky="w")

    symbols_var = tk.BooleanVar()
    symbols_checkbutton = tk.Checkbutton(main_frame, text="Symbols", variable=symbols_var, bg="#f0f0f0")
    symbols_checkbutton.grid(row=4, column=0, sticky="w")

    generate_button = tk.Button(main_frame, text="Generate Password", command=generate, bg="#55acee", fg="white")
    generate_button.grid(row=5, column=0, columnspan=2, pady=5)

    generated_password_label = tk.Label(main_frame, text="Generated Password:", bg="#f0f0f0")
    generated_password_label.grid(row=6, column=0, sticky="w")
    generated_password_entry = tk.Entry(main_frame, width=30)
    generated_password_entry.grid(row=7, column=0, columnspan=2)

    copy_button = tk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard, bg="#55acee", fg="white")
    copy_button.grid(row=8, column=0, columnspan=2, pady=5)

    root.mainloop()

generate_password_gui()
