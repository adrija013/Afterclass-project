import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Weak Password", "Password length should be at least 4.")
            return

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        all_chars = lower + upper + digits + symbols


        password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(symbols)
        password += ''.join(random.choices(all_chars, k=length - 4))

        password = ''.join(random.sample(password, len(password)))

        password_var.set(password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)
tk.Label(frame, text="Enter password length:", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT)
length_entry = tk.Entry(frame, width=5, font=("Arial", 12))
length_entry.pack(side=tk.LEFT, padx=10)
length_entry.insert(0, "12") 

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=30, justify='center')
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_password).pack(pady=10)

root.mainloop()